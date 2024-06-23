import ollama 
from tqdm import tqdm
from .logger import logger
from comfy.utils import ProgressBar

class GenerateOllama:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_name": ("STRING", {"default": "phi3"}),
                "tag": ("STRING", {"default": "latest"}),
                "prompt": ("STRING", {"default": "Why is the sky blue?"}),
            },
        }

    @classmethod
    def IS_CHANGED(s):
        return float("NaN") # Always execute the node.


    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output_text",)

    CATEGORY = "LLM/Ollama"

    FUNCTION = "generate"
    def generate(self, model_name, tag, prompt):

        # if tag does not begin with : then add : to the string
        if not tag.startswith(":"):
            tag = ":" + tag
        model_name_full = model_name + tag
        model_name_full = model_name_full.strip() # trim whitespace from before and after model_name_full

        response = ollama.generate(model_name_full, prompt)
        
        return ()