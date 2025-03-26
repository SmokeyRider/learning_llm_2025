# Repository: Learning Python

This repository contains various Python scripts created while learning Python. These scripts are designed to run AI models via Ollama and explore different Python concepts.

- This repository is a work in progress and is updated as new concepts are learned.
- Contributions or suggestions are welcome!


## Scripts Overview

### `chatbot.py`
A web-based chatbot script designed for interacting with AI models. It is the latest generation of the script for web-based chat functionality.

**This script requires Ollama to be installed and running.** 

### `Odin_3.py`
A terminal-based chatbot script for interacting with AI models.  It is the latest generation of the script for terminal-based chat functionality.

**This script requires Ollama to be installed and running.** 

### `cars.py`
A script for experimenting with Python object manipulation. It includes examples of working with classes, objects, and methods.

### `categorizer.py`
A script that reads a file containing a list of grocery items and categorizes them using hardcoded values. This script is based on a YouTube tutorial and demonstrates basic file handling and categorization logic.

### `nines.py`
A script that prints the multiplication table for the number 9. This script is a simple demonstration of loops and basic arithmetic in Python.

### `Jupyter_nb.ipynb`
A Jupyter Notebook containing examples and experiments with Python code. This notebook is used for interactive learning and exploring Python concepts.

### Codespaces Configuration
This repository is pre-configured to work seamlessly with GitHub Codespaces. However, **Ollama still needs to be installed and run manually** within the Codespaces environment. Additionally, ensure that the required AI models are "pulled" down using Ollama before running any scripts that depend on them.

### Starting the Ollama Service
Use the `start_ollama.sh` script to start the Ollama service:
```bash
bash start_ollama.sh
```

### Pulling AI Models
Before running scripts that interact with AI models, ensure the required models are pulled using Ollama:
```bash
ollama pull <model_name>
```
Replace `<model_name>` with the name of the AI model you want to use.

### Setting up a vitural Python environment 
This maybe good idea if not running in Codepsaces.
Setup virtual python in Powershell:
```powershell
    python -m venv myenv
    myenv\scripts\activate
```