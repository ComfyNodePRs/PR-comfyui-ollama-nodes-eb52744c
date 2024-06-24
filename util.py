from .logging_setup import setup_logging
import logging

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
            },
            "optional": {
                "delimiter": ("STRING", {}),
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

    def list_to_string(self, list, delimiter):

        output_string = ""
        for element in list:
            output_string += str(element) # cast so we can handle non-string inputs
            if delimiter:
                output_string += delimiter
        return (output_string,)
    

class BooleanToString:
    def __init__(self):
        setup_logging()
        self.logger = logging.getLogger("comfyui-ollama-nodes.BooleanToString")

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "boolean_value": ("BOOLEAN", {"forceInput": True}),
            }
        }

    @classmethod
    def IS_CHANGED(s):
        return float("NaN")  # Always execute the node.

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string_value",)

    FUNCTION = "convert_boolean_to_string"

    CATEGORY = "Utility"

    def convert_boolean_to_string(self, boolean_value):
        self.logger.debug(f"Converting boolean value: {boolean_value}")
        string_value = "True" if boolean_value else "False"
        self.logger.debug(f"Converted string value: {string_value}")
        return (string_value,)

class FloatToString:
    def __init__(self):
        setup_logging()
        self.logger = logging.getLogger("comfyui-ollama-nodes.FloatToString")

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "float_value": ("FLOAT", {"forceInput": True}),
            }
        }

    @classmethod
    def IS_CHANGED(s):
        return float("NaN")  # Always execute the node.

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string_value",)

    FUNCTION = "convert_float_to_string"

    CATEGORY = "Utility"

    def convert_float_to_string(self, float_value):
        self.logger.debug(f"Converting float value: {float_value}")
        string_value = str(float_value)
        self.logger.debug(f"Converted string value: {string_value}")
        return (string_value,)
    
class IntToString:
    def __init__(self):
        setup_logging()
        self.logger = logging.getLogger("comfyui-ollama-nodes.IntToString")

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "int_value": ("INT", {"forceInput": True}),
            }
        }

    @classmethod
    def IS_CHANGED(s):
        return float("NaN")  # Always execute the node.

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string_value",)

    FUNCTION = "convert_int_to_string"

    CATEGORY = "Utility"

    def convert_int_to_string(self, int_value):
        self.logger.debug(f"Converting int value: {int_value}")
        string_value = str(int_value)
        self.logger.debug(f"Converted string value: {string_value}")
        return (string_value,)
