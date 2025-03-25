FROM mcr.microsoft.com/devcontainers/python:3.12-bookworm

COPY requirements.txt /tmp/pip-tmp/

RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

# Install prerequisites for Ollama (if required)
RUN apt-get update && apt-get install -y curl

# Install Ollama (replace with the actual installation command from Ollama's documentation)
RUN curl -fsSL https://ollama.com/install.sh | bash

# Clean up to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*