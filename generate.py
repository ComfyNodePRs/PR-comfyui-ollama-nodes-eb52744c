import ollama
from comfy.utils import ProgressBar
from .logging_setup import setup_logging
import logging

import torch
import numpy as np
from io import BytesIO
from PIL import Image



class GenerateOllama:
    def __init__(self):
        setup_logging()
        self.logger = logging.getLogger("comfyui-ollama-nodes.GenerateOllama")
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_name": ("STRING", {"default": "llava:latest"}),
                "prompt": ("STRING", {"default": "Describe the images", "multiline":True}),
                "system": ("STRING", {"default": "You are an AI assitant that describes images in great detail, focusing on the lighting, mood, scene, details, subjects, hues, and colors","multiline":True}),
                "stream": ("BOOLEAN", {"default": False}),
                
            },
            "optional": {
                "template": ("STRING", {"default": ""}),
                "format": ("STRING", {"default": ""}),
                "context": ("LIST", {"element_type": "INTEGER"}),
                "images": ("IMAGE", {}),
                "options": ("DICTIONARY", {"default": {}}),
                "keep_alive": ("FLOAT", {"default": 0}), # -1 means keep model loaded forever, new models are replaced if necessary
            }
        }

    @classmethod
    def IS_CHANGED(s):
        return float("NaN")  # Always execute the node.

    RETURN_TYPES = ("STRING", 
                    "STRING", 
                    "STRING",
                    "BOOLEAN", 
                    "STRING", 
                    "LIST", 
                    "FLOAT", 
                    "FLOAT", 
                    "FLOAT", 
                    "INT", 
                    "FLOAT")
    RETURN_NAMES = ("response", 
                    "model", 
                    "created_at", 
                    "done", 
                    "done_reason", 
                    "context", 
                    "total_duration", 
                    "load_duration",
                    "prompt_eval_duration", 
                    "eval_count", 
                    "eval_duration")

    FUNCTION = "generate_text"

    CATEGORY = "LLM/Ollama"





    def convert_images_to_png(self, image_tensor):
        """
        Convert a batch of images to a list of PNG-encoded BytesIO objects.

        Args:
        - image_tensor (torch.Tensor or np.ndarray): A tensor of shape [B, H, W, C].

        Returns:
        - image_list_png (list): A list of BytesIO objects containing PNG-encoded images.
        """
        if isinstance(image_tensor, np.ndarray):
            image_tensor = torch.tensor(image_tensor)

        # Ensure the image tensor has the correct shape
        assert len(image_tensor.shape) == 4, "Image tensor must have shape [B, H, W, C]"
        B, H, W, C = image_tensor.shape
        assert C == 3, "Image tensor must have 3 channels (RGB)"

        image_list_png = []

        for i in range(B):
            image = image_tensor[i].cpu().numpy()
            image = (image * 255).astype(np.uint8)  # Assuming the tensor values are in [0, 1]
            image_pil = Image.fromarray(image)
            image_io = BytesIO()
            image_pil.save(image_io, format='PNG')
            image_io.seek(0)
            image_list_png.append(image_io)

        return image_list_png

    def generate_text(self, model_name, prompt, system, template, stream, format, context=None, images=None, options=None, keep_alive=None):
        self.logger.info(f"Generating text with model: {model_name}")
        self.logger.debug(f"Prompt: {prompt}")
        self.logger.debug(f"System: {system}")
        self.logger.debug(f"Template: {template}")
        self.logger.debug(f"Context: {context}")
        self.logger.debug(f"Stream: {stream}")
        self.logger.debug(f"Format: {format}")
        self.logger.debug(f"Images: {images}")
        self.logger.debug(f"Options: {options}")
        self.logger.debug(f"Keep Alive: {keep_alive}")

        if images is not None and len(images) > 0:
            images = self.convert_images_to_png(images) # Convert the tensor to a BytesIO object

        
        if stream:
            generated_text = ""
            for response in ollama.generate(
                model=model_name,
                prompt=prompt,
                system=system,
                template=template,
                context=context,
                stream=stream,
                raw=False,
                format=format,
                images=images,
                options=options,
                keep_alive=keep_alive,
            ):
                generated_text += response.get('text', '')
                pbar = ProgressBar(len(generated_text))
                pbar.update(len(response.get('text', '')))
            final_response = {
                "model": model_name,
                "created_at": response.get('created_at', ''),
                "response": generated_text,
                "done": response.get('done', True),
                "done_reason": response.get('done_reason', 'stop'),
                "context": response.get('context', []),
                "total_duration": response.get('total_duration', 0.0),
                "load_duration": response.get('load_duration', 0.0),
                "prompt_eval_duration": response.get('prompt_eval_duration', 0.0),
                "eval_count": response.get('eval_count', 0),
                "eval_duration": response.get('eval_duration', 0.0)
            }
        else:
            response = ollama.generate(
                model=model_name,
                prompt=prompt,
                system=system,
                template=template,
                context=context,
                stream=stream,
                raw=False,
                format=format,
                images=images,
                options=options,
                keep_alive=keep_alive,
            )
            final_response = {
                "model": response.get('model', ''),
                "created_at": response.get('created_at', ''),
                "response": response.get('response', ''),
                "done": response.get('done', True),
                "done_reason": response.get('done_reason', 'stop'),
                "context": response.get('context', []),
                "total_duration": response.get('total_duration', 0.0),
                "load_duration": response.get('load_duration', 0.0),
                "prompt_eval_duration": response.get('prompt_eval_duration', 0.0),
                "eval_count": response.get('eval_count', 0),
                "eval_duration": response.get('eval_duration', 0.0)
            }

        return (
            final_response["response"],
            final_response["model"],
            final_response["created_at"],
            final_response["done"],
            final_response["done_reason"],
            final_response["context"],
            final_response["total_duration"],
            final_response["load_duration"],
            final_response["prompt_eval_duration"],
            final_response["eval_count"],
            final_response["eval_duration"],
        )
