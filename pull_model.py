import ollama 
from tqdm import tqdm
from .logger import logger
from comfy.utils import ProgressBar

class PullModel:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_name": ("STRING", {"default": "phi3"}),
                "tag": ("STRING", {"default": "latest"}),
                "stream": ("BOOLEAN", {"default":"false"},),
            },
        }

    @classmethod
    def IS_CHANGED(s):
        return float("NaN")


    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES = ("output_text","model_name",)

    FUNCTION = "pull_model"

    #OUTPUT_NODE = False

    CATEGORY = "LLM/Ollama"

    def pull_model(self, model_name, tag, stream):

        # if tag does not begin with : then add : to the string
        if not tag.startswith(":"):
            tag = ":" + tag

        model_name_full = model_name + tag
        model_name_full = model_name_full.strip() # trim whitespace from before and after model_name_full
        logger.info("Pulling model: " + model_name_full)


        if stream:
            current_digest, bars = '', {}
            
            for progress in ollama.pull(model_name_full, stream=True):
                total = progress.get('total', 100)
                logger.info(f"total: {total}")
                completed = progress.get('completed', 0)
                logger.info(f"completed: {completed}")
                pbar = ProgressBar(total) # Set the total size of the progress bar
                pbar.update(completed) # Update the progress bar with the completed size so far
                digest = progress.get('digest', '')
                if digest != current_digest and current_digest in bars:
                    bars[current_digest].close()

                if not digest:
                    logger.info(progress.get('status'))
                    continue

                if digest not in bars and (total := progress.get('total')):
                    bars[digest] = tqdm(total=total, desc=f'pulling {digest[7:19]}', unit='B', unit_scale=True)

                if completed := progress.get('completed'):
                    bars[digest].update(completed - bars[digest].n)

                current_digest = digest
        else:
            response = ollama.pull(model_name_full, stream=stream)
            # Non-streaming scenario: handle the single response
            if 'completed' in response and 'total' in response:
                logger.info(f"Download completed: {response['completed']} out of {response['total']} ({response['status']})")

        pull_result = "Model downloaded successfully"
        return (pull_result, model_name_full,)

