from .pull_model import PullModel
from .download_huggingface_models import DownloadHuggingfaceModel
from .list_models import ListModels, ListToString
from .generate import GenerateOllama

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "PullModel": PullModel,
    "ListModels": ListModels,
    "DownloadHuggingfaceModel": DownloadHuggingfaceModel,
    "GenerateOllama": GenerateOllama,
    "ListToString": ListToString
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "PullModel":"Pull Model | Ollama Nodes",
    "ListModels":"List Models | Ollama Nodes",
    "ListToString":"List to String | Ollama Nodes",
    "DownloadHuggingfaceModel":"Download Huggingface Model | Ollama Nodes",
    "GenerateOllama":"Generate Text | Ollama Nodes"
    
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 