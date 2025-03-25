#!/bin/bash

# Check if Ollama is installed
if ! command -v ollama &>/dev/null; then
  echo "Ollama is not installed. Please install it before proceeding."
  exit 1
fi

echo "Starting Ollama service..."
# Start Ollama in the background
ollama serve 

# Optionally, wait a few seconds for the service to become ready
sleep 2

# Optional: Output the running processes for confirmation
ollama ps