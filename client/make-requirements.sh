#!/bin/bash

python3 -m venv ollama-client-1
source ollama-client-1/bin/activate &&
pip3 install ollama==0.3.1 &&
pip3 freeze > requirements.txt
