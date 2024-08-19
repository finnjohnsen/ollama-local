#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate &&
pip3 install ollama==0.3.1 psutil &&
pip3 freeze > requirements.txt
