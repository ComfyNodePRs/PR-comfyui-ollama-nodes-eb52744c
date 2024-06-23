import ollama 
from .logging_setup import setup_logging
import logging

class ListModels:
    def __init__(self):
        setup_logging()
        self.logger = logging.getLogger("comfyui-ollama-nodes.ListModels")
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "delimiter": ("STRING", {"default": ","}),
            }
        }

    @classmethod
    def IS_CHANGED(s):
        return float("NaN") # Always execute the node.


    RETURN_TYPES = ("LIST","STRING")
    RETURN_NAMES = ("model_list","model_list_as_string")

    FUNCTION = "list_models"

    #OUTPUT_NODE = False

    CATEGORY = "LLM/Ollama"

    def list_models(self, delimiter: str):

        # UI shows \\n as \n, \\t as \t
        if delimiter.startswith("\\"): # converts \\n to \n, \\t to \t, etc.
            
            print(delimiter)

        response = ollama.list()
        model_name_list = []
        for model in response['models']:
            model_name_list.append(model["name"])
        model_list_delimited = delimiter.join(model_name_list)
        return (model_name_list, model_list_delimited,)

# cannot use StringListToString becuase class names must be globally unique
# and StringListToString is already used in ComfyUI-Impact-Pack
class ListToString: 
    def __init__(self):
        setup_logging()
        self.logger = logging.getLogger("comfyui-ollama-nodes.ListModels")
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "list": ("LIST", {"forceInput": True}),
            }
        }

    @classmethod
    def IS_CHANGED(s):
        return float("NaN") # Always execute the node.


    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)

    FUNCTION = "list_to_string"

    #OUTPUT_NODE = False

    CATEGORY = "LLM/Ollama"

    def list_to_string(self, list):

        output_string = ""
        for element in list:
            output_string += str(element) # cast so we can handle non-string inputs
        return (output_string,)