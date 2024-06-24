from .pull_model import PullModel
from .download_huggingface_models import DownloadHuggingfaceModel
from .list_models import ListModels
from .util import ListToString, BooleanToString, FloatToString, IntToString
from .generate import GenerateOllama

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "PullModel": PullModel,
    "ListModels": ListModels,
    "DownloadHuggingfaceModel": DownloadHuggingfaceModel,
    "GenerateOllama": GenerateOllama,
    "ListToString": ListToString,
    "BooleanToString": BooleanToString,
    "FloatToString": FloatToString,
    "IntToString": IntToString
}

package_name = "| Ollama Nodes"

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "PullModel":f"Pull Model {package_name}",
    "ListModels":f"List Models {package_name}",
    "ListToString":f"List to String {package_name}",
    "DownloadHuggingfaceModel":f"Download Huggingface Model {package_name}",
    "GenerateOllama":f"Generate Text {package_name}",
    "BooleanToString":f"Boolean to String {package_name}",
    "FloatToString":f"Float to String {package_name}",
    "IntToString":f"Int to String {package_name}",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 