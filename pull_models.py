import subprocess

model_names: list = ["deepseek-r1", "phi4", "phi3", "gemma3", "llama3.3", "llama3.2", "mistral"]

def pull_model(model):
    command = f'ollama pull {model}'
    print(f'Executing: {command}')
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f'Success: {model} {result.stdout}')
    else:
        print(f'Error: {model}: {result.stderr}')

# Run commands serially
for model in model_names:
    pull_model(model)

# Run "ollama list" after all models are pulled
print("\nExecuting: ollama list")
result = subprocess.run("ollama list", shell=True, capture_output=True, text=True)
if result.returncode == 0:
    print(f'Success: \n{result.stdout}')
else:
    print(f'Error: \n{result.stderr}')
