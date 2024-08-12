# start server. no model loaded
run-server:
	podman run --rm  --device nvidia.com/gpu=all -v /home/finn/ollama/ollama-volume:/root/.ollama -p 11434:11434 --name ollama ollama/ollama:0.3.5 

# watch GPU
w-gpu:
	gpustat -i 2 --no-processes

# prompts inside container
llama:
	podman exec -it ollama ollama run llama3.1

mistral-nemo:
	podman exec -it ollama ollama run mistral-nemo

