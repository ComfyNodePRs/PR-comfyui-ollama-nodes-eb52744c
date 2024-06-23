import ollama 
from tqdm import tqdm
from .logging_setup import setup_logging
import logging
from comfy.utils import ProgressBar

class PullModel:
    def __init__(self):
        setup_logging()
        self.logger = logging.getLogger("comfyui-ollama-nodes.PullModel")
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_name": ("STRING", {"default": "phi3:latest"}),
                "stream": ("BOOLEAN", {"default":"false"},),
            },
        }

    @classmethod
    def IS_CHANGED(s):
        return float("NaN") # Always execute the node.


    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES = ("output_text","model_name",)

    FUNCTION = "pull_model"

    #OUTPUT_NODE = False

    CATEGORY = "LLM/Ollama"

    def pull_model(self, model_name, stream):

        model_name = model_name.strip() # trim whitespace
        self.logger.info("Pulling model: " + model_name)


        if stream:
            current_digest, bars = '', {}
            
            for progress in ollama.pull(model_name, stream=True):
                total = progress.get('total', 100)
                #self.logger.debug(f"total: {total}")
                completed = progress.get('completed', 0)
                #self.logger.debug(f"completed: {completed}")

                # Update the ComfyUI node progress bar
                pbar = ProgressBar(total) # Set the total size of the progress bar
                pbar.update(completed) # progress bar with the completed size so far
                
                # Update the progress bar in the logs
                digest = progress.get('digest', '') # digest is the unique identifier for the progress bar
                if digest != current_digest and current_digest in bars: # Close the progress bar if the digest has changed
                    bars[current_digest].close()

                if not digest: # If there is no digest, then log the status and continue
                    self.logger.info(progress.get('status'))
                    continue

                if digest not in bars and (total := progress.get('total')): # If the digest is not in the bars and there is a total, then create a new progress bar
                    bars[digest] = tqdm(total=total, desc=f'pulling {digest[7:19]}', unit='B', unit_scale=True)

                if completed := progress.get('completed'): # If there is a completed size, then update the progress bar
                    bars[digest].update(completed - bars[digest].n)

                current_digest = digest
        else:
            response = ollama.pull(model_name, stream=stream)
            # Non-streaming scenario: handle the single response
            if 'completed' in response and 'total' in response:
                self.logger.info(f"Download completed: {response['completed']} out of {response['total']} ({response['status']})")

        pull_result = "Model downloaded successfully"
        return (pull_result, model_name,)

