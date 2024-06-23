# comfyui-ollama-nodes

ComfyUI custom nodes for working with [Ollama](https://github.com/ollama/ollama). Assumes that an Ollama server is running at `http://127.0.0.1:11434` and accessible by the ComfyUI backend.

## TODO:
- [X] Implement model pulling node
    - [ ] Implement UI progress bar updates when pulling with `stream=True`
- [x] Impelement Huggingface Hub model downloader node
- [ ] Implement model loading node
- [ ] Implement completion node
- [ ] Implement completion node with vision model
- [ ] Implement chat node
- [ ] Implement [model converter](https://github.com/ggerganov/llama.cpp/discussions/2948) node (saftetensor to GGUF)
- [ ] Implement quantization node 

## Similar Nodes
The following node packs are similar and effort will be made to integrate seemlessly with them:
- https://github.com/daniel-lewis-ab/ComfyUI-Llama
- https://github.com/get-salt-AI/SaltAI_Language_Toolkit
- https://github.com/alisson-anjos/ComfyUI-Ollama-Describer


## Development

If you'd like to contribute, please open a Git Issue describing what you'd like to contribute. See ComfyOrg docs for instructions on getting started [developing custom nodes](https://docs.comfy.org/essentials/custom_node_overview).

## Attributions

- logger.py taken from https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite, GPL-3.0 license 