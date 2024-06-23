import logging
import huggingface_hub 
from typing import Optional, Union, Literal
from pathlib import Path
from .logger import logger

class DownloadHuggingfaceModel:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "repo_id": ("STRING", {"default": "microsoft/Phi-3-mini-4k-instruct-gguf"}),
                "filename": ("STRING", {"default": "Phi-3-mini-4k-instruct-q4.gguf"}),
                "local_dir": ("STRING", {"default": "./models/llm/"}),
            },
            # "optional": { # TOOD: Figure out why optional doesn't work
            #     "subfolder": ("STRING",),
            #     "repo_type": ("STRING",),
            #     "revision": ("STRING",),
            #     "cache_dir": ("STRING",),
            #     "force_download": ("BOOLEAN", {"default": False}),
            #     "token": ("STRING", ),
            # }
        }

    @classmethod
    def IS_CHANGED(s):
        return float("NaN")


    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output_text",)

    FUNCTION = "download_model"

    #OUTPUT_NODE = False

    CATEGORY = "LLM/Ollama"

    def download_model(self,
        repo_id: str,
        filename: str,
        subfolder: Optional[str] = None,
        repo_type: Optional[str] = None,
        revision: Optional[str] = None,
        cache_dir: Union[str, Path, None] = None,
        local_dir: Union[str, Path, None] = None,
        force_download: bool = False,
        token: Union[bool, str, None] = None,

    ) -> str:
        #logger.error(f"repo_type: {repo_type}")
        huggingface_hub.hf_hub_download(repo_id=repo_id, 
                                        filename=filename, 
                                        subfolder=subfolder, 
                                        repo_type=repo_type, 
                                        revision=revision,
                                        cache_dir=cache_dir, 
                                        local_dir=local_dir,
                                        force_download=force_download,
                                        token=token)

        return "Model downloaded successfully"


