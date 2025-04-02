# Repository: Learning LLMs

This repository contains various Python scripts created while learning LLMs with Python. These scripts are designed to run AI models via Ollama and explore different Python concepts.

- This repository is a work in progress and is updated as new concepts are learned.
- Contributions or suggestions are welcome!

## Scripts Overview

### `chatbot.py`
A web-based chatbot script designed for interacting with AI models. It is the latest generation of the script for web-based chat functionality.

**This script requires Ollama to be installed and running.** 

### `Odin_3.py`
A terminal-based chatbot script for interacting with AI models.  It is the latest generation of the script for terminal-based chat functionality.

**This script requires Ollama to be installed and running.** 

### `categorizer.py`
A script that reads a file containing a list of grocery items and categorizes them using hardcoded values. This script is based on a YouTube tutorial and demonstrates basic file handling and categorization logic.

### Codespaces/Dev Container Configuration
This repository is pre-configured to work seamlessly with Dev Containers & GitHub Codespaces. Ollama is installed and running by default in the container image. However the required AI models need to be "pulled" down using Ollama before running any scripts that depend on them.  The pull_models.py script is a convinient way pull a set of typical models

### Setting up a vitural Python environment 
This maybe good idea if not running in Codepsaces.
Setup virtual python in Powershell:
```powershell
    python -m venv myenv
    myenv\scripts\activate
```