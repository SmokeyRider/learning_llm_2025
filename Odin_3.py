from colorama import init, Fore, Style
from ollama import list as ollama_list, chat as ollama_chat  # Import specific functions

# Initialize colorama
init(autoreset=True)

# Get list of available models
try:
    model_set = ollama_list()
except Exception as e:
    print(Fore.RED + "An error occurred listing Ollama models:", str(e))
    exit(1)

# Initialize an empty list to store the simplified model names
model_names = []

# Iterate over the list and get simplified model names
print(Fore.GREEN + "Available models: ", end="")
for model in model_set.models:
    model_name = model.model.split(":")[0]  # Split the string at ":" and take the first part
    model_names.append(model_name)  # Append the processed model name to the list
    print(Fore.GREEN + f"{model_name}", end=" ", flush=True)

# Set default values
DEFAULT_MODEL = "llama3.2"
DEFAULT_SYSTEM_STR = "You are Odin's helpful assistant."
DEFAULT_PROMPT = "what is a mole?"
DEFAULT_TEMP = 0.7
DEFAULT_STREAMING = True

model_str = DEFAULT_MODEL
system_str = DEFAULT_SYSTEM_STR
prompt_str = DEFAULT_PROMPT
temp_flt = DEFAULT_TEMP
streaming_output = DEFAULT_STREAMING

# Initialize conversation history
conversation_history = [
    {"role": "system", "content": system_str}
]
# Prompt model overrides
while True:
    model_str = input(f"\nModel \"{model_str}\": ").strip() or model_str
    if model_str.lower() in (name.lower() for name in model_names):
        break
    else:
        print(Fore.RED + f"Model \"{model_str}\" Not valid.")
        print(Fore.GREEN + "Available models: ", end="")
        for model in model_set.models:
            model_name = model.model.split(":")[0]  # Split the string at ":" and take the first part
            model_names.append(model_name)  # Append the processed model name to the list
            print(Fore.GREEN + f"{model_name}", end=" ", flush=True)

# Prompt for temperature overrides with validation
while True:
    try:
        temp_flt = float(input(f"Temperature \"{temp_flt}\": ").strip() or temp_flt)
        if 0 <= temp_flt <= 1:
            break
        else:
            print(Fore.RED + "Temperature must be between 0 and 1. Please try again.")
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number between 0 and 1.")

# Prompt for prompt overrides
prompt_str = input(f"Prompt \"{prompt_str}\": ").strip() or prompt_str

def chat_with_model(prompt):
    """
    Function to chat with the model.
    """
    try:
        conversation_history.append({"role": "user", "content": prompt})
        response = ollama_chat(
            model=model_str,
            messages=conversation_history,
            stream=streaming_output,
            options={'temperature': temp_flt} # very conservative (good for coding and correct syntax)
        )
        
        # Initialize a list to collect the response chunks
        response_chunks = []
        
        print(Fore.CYAN + "Assistant: ", end="", flush=True)
        for chunk in response:
            chunk_content = chunk['message']['content']
            print(Fore.CYAN + chunk_content, end="", flush=True)
            response_chunks.append(chunk_content)
        
        # Combine all chunks into a single response
        full_response = ''.join(response_chunks)
        conversation_history.append({"role": "assistant", "content": full_response})
    except Exception as e:
        print(Fore.RED + "\n\nA chat error occurred:", str(e))
        exit(1)

# Allow repeated prompts
while True:
    chat_with_model(prompt_str)
    prompt_str = input("\n\nPrompt: ").strip()
    if prompt_str.lower() in ["exit", "quit", ""]:
        break
exit(0)