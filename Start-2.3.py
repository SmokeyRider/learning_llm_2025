import ollama # Import the ollama library

# List available models
model_set = ollama.list()
#print(f"{model_set.models[0]} \n\n")

# Initialize an empty list to store the processed model names
model_names = []

# Iterate over the list and print the "model" values
print("Available models:")
for model in model_set.models:
    model_name = model.model.split(":")[0]  # Split the string at ":" and take the first part
    model_names.append(model_name)  # Append the processed model name to the list
    print(f"\t {model_name}")

# Set default values
model_str = "llama3.2" # Specify the default model to use
system_str = "You are Odin's helpful assistant."
prompt_str = "what is a mole?" # Prompt string for the model
stream_output = True # Set to False for non-streaming output

# prompt for user input overrides
model_str = input(f"Model \"{model_str}\": ").strip() or model_str
if not model_str.lower() in (name.lower() for name in model_names):
    print(f"FATAL ERROR: Model \"{model_str}\" is not available.")
    exit(1)
prompt_str = input(f"Prompt \"{prompt_str}\": ").strip() or prompt_str

# Create a custom model file
modelfile_str = """
FROM """+model_str+"""
SYSTEM """+system_str+"""
PARAMETER temperature 0.9
"""

#ollama.create(model="knowitall", modelfile=modelfile_str)

print()

try:
    # Generate a response from the custom model
    res = ollama.generate(
        model=model_str,  # Specify the model to use
        prompt=prompt_str,  # User's prompt
        stream=stream_output,  # Enable streaming
    )

    if stream_output:
        #streamed output
        for chunk in res:
            print(chunk["response"], end='', flush=True)
    else:
        #raw output
        print(res["response"])

except Exception as e:
    print("An error occurred: ", str(e))
