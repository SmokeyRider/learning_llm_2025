
import ollama # Import the ollama library

# Uncomment the following lines to list available models
# response = ollama.list()
# print(response)

# Basic control of the chat conversation
modelName = "llama3.2" # Specify the model to use
streamedOUtput = True # Set to False for non-streaming output
promptStr = "tell me about PEP 8." # Prompt string for the model
messageString = [ #Control the chat conversation
    {"role": "system", "content": "You are Odin's helpful assistant."},
    {"role": "assistant", "content": "I am an AI model created by Odin."},
    {"role": "user", "content": "I am Odin. "+promptStr},
]

res = ollama.chat(
    model=modelName,  # Specify the model to use
    messages=messageString,  # User's message
    stream=streamedOUtput,  # Enable streaming
)

if streamedOUtput:
    #streamed output
    for chunk in res:
        print(chunk["message"]["content"], end='', flush=True)
else:
    #raw output
    print("Model: ",res["model"])
    print("Role: ",res["message"]["role"])
    print("Content: ")
    print()
    print(res["message"]["content"])



