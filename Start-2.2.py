
import ollama # Import the ollama library

# Uncomment the following lines to list available models
# response = ollama.list()
# print(response)

# Set default values
model_str = "llama3.2" # Specify the default model to use
system_str = "You are Odin's helpful assistant."
prompt_str = "Where are we?" # Prompt string for the model
stream_output = True # Set to False for non-streaming output

# allow for user input overides
model_str = input(f"Model \"{model_str}\": ").strip() or model_str
prompt_str = input(f"Prompt \"{prompt_str}\": ").strip() or prompt_str

# create a custom modle file
modelfile_str = """
FROM """+model_str+"""
SYSTEM """+system_str+"""
PARAMETER temperature 0.9
"""



#ollama.create(model="knowitall", modelfile=modelfile_str)

# Generate a response from the custom model
res = ollama.generate(
    model=model_str,  # Specify the model to use
    prompt=prompt_str,  # User's prompt
    stream=stream_output,  # Enable streaming
)

# Print the response
print("Response: ")

if stream_output:
    #streamed output
    for chunk in res:
        print(chunk["response"], end='', flush=True)
else:
    #raw output
    print(res["response"])




