# Run like: python -m custom_nodes.comfyui-ollama-nodes.tests from the ComfyUI directory
import sys
import os
from .pull_model import PullModel
from .download_huggingface_models import DownloadHuggingfaceModel

import ollama

#from pull_model import PullModel

def test_pull_model():
    model_puller = PullModel()
    model_puller.pull_model("phi3", "latest", stream=True)

def test_download_huggingface_models():
    model_downloader = DownloadHuggingfaceModel()
    model_downloader.download_model(repo_id="microsoft/Phi-3-mini-4k-instruct-gguf", 
                                    filename="Phi-3-mini-4k-instruct-q4.gguf", 
                                    local_dir="./models/llm/")
    # check that the file is downloaded
    assert os.path.exists("./models/llm/Phi-3-mini-4k-instruct-q4.gguf")

if __name__ == "__main__":
    #test_pull_model()
    #test_download_huggingface_models()

    response = ollama.list()
    model_name_list = []
    for model in response['models']:
        #print(model)
        model_name_list.append(model["name"])
    #print(model_name_list)
    # print model_name_list with newline delimination
    print("\n".join(model_name_list))
