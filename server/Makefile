ifeq ($(shell command -v podman 2> /dev/null),)
    DOCKER=docker
else
    DOCKER=podman
endif

OS := $(shell uname)

os-check-sanity:
	@if [ "Linux" = $(OS) ]; then \
		echo "Linux"; \
	fi
	@if [ "Darwin" = $(OS) ]; then \
		echo "MacOS"; \
	fi

# remove -d to prevent detach
run-server:
	-mkdir -p ${HOME}/.ollama-workdir
	${DOCKER} run -d --rm  --device nvidia.com/gpu=all -v ${HOME}/.ollama-workdir:/root/.ollama -p 11434:11434 --name ollama ollama/ollama:0.3.5 

# watch GPU (Linux)
w-gpu:
	gpustat -i 2 --no-processes

# prompts inside container

bash:
	${DOCKER} exec -it ollama /bin/bash

llama:
	${DOCKER} exec -it ollama ollama run llama3.1

mistral-nemo:
	${DOCKER} exec -it ollama ollama run mistral-nemo

tinyllama:
	${DOCKER} exec -it ollama ollama run tinyllama

starcoder3b:
	${DOCKER} exec -it ollama ollama run starcoder2:3b

starcoder7b:
	${DOCKER} exec -it ollama ollama run starcoder2:7b

codellama7b:
	${DOCKER} exec -it ollama ollama run codellama:7b

codellama13b:
	${DOCKER} exec -it ollama ollama run codellama:13b
