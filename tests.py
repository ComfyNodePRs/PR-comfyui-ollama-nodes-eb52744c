# Run from the ComfyUI root directory with
# python -m custom_nodes.comfyui-ollama-nodes.tests from the ComfyUI directory
import sys
import os
from .pull_model import PullModel
from .download_huggingface_models import DownloadHuggingfaceModel
from .list_models import ListModels
from .generate import GenerateOllama

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

def test_list_models():
    lister = ListModels()
    response = lister.list_models(delimiter="\n")
    print(response)

def test_generate():
    generator = GenerateOllama()
    response = generator.generate("phi3:latest", "Why is the sky blue?")
    print(response)

if __name__ == "__main__":
    #test_pull_model()
    #test_download_huggingface_models()
    #test_list_models()
    
    
    model_name = "phi3:latest"
    prompt="why is the sky blue?"
    response = ollama.generate(model_name, prompt)
    print(response["response"])
    print(response.keys())