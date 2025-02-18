from ollama import list as ollama_list, chat as ollama_chat  # Import specific functions
from colorama import init, Fore, Style

# Set default values
DEFAULT_MODEL: str = "llama3.2"
DEFAULT_SYSTEM_STR: str = "You are Odin's helpful assistant."
DEFAULT_PROMPT: str = "I am Odin, the All-Father.  Where do I live?"
DEFAULT_TEMP: float = 0.7
DEFAULT_STREAMING: bool = True
MIN_TEMP: int = 0
MAX_TEMP: int = 1

# Initialize variables with default values
model_str: str = DEFAULT_MODEL
system_str: str = DEFAULT_SYSTEM_STR
prompt_str: str = DEFAULT_PROMPT
temp_flt: float = DEFAULT_TEMP
streaming_output: bool = DEFAULT_STREAMING
model_names: list = [] #empty list to store model names

# Initialize colorama
init(autoreset=True)

# Get list of available models
try:
    model_set = ollama_list()
except Exception as e:
    print(Fore.RED + "An error occurred listing Ollama models:", str(e))
    exit(1)

# Iterate over the list and populate a list of model names
print(Fore.GREEN + "Available models: ")
for model in model_set.models:
    model_name = model.model  
    model_names.append(model_name)  # Append the processed model name to the list

model_names.sort()  # Sort the list of model names alphabetically

# Print the list of model names
for name in model_names:
    print(Fore.GREEN + f"\t{name}", flush=True)

# Prompt model overrides
while True:
    model_str = input(f"Model \"{model_str}\": ") or model_str
    if  ":" not in model_str: # add ":latest" if not specified
        model_str = model_str + ":latest"
    if model_str.lower() in (name.lower() for name in model_names):
        break
    else:
        print(Fore.RED + f"Model \"{model_str}\" Not valid.")
        print(Fore.GREEN + "Available models: ")
        for name in model_names:
            print(Fore.GREEN + f"\t{name}", flush=True)

# Prompt for temperature overrides with validation
while True:
    try:
        temp_flt = float(input(f"Temperature \"{temp_flt}\": ") or temp_flt)
        if MIN_TEMP <= temp_flt <= MAX_TEMP:
            break
        else:
            print(Fore.RED + f"Temperature must be between {MIN_TEMP} and {MAX_TEMP}. Please try again.")
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number between 0 and 1.")

# prompt for system string overrides
system_str = input(f"System Prompt \"{system_str}\": ").strip() or system_str

# Prompt for prompt overrides
prompt_str = input(f"User Prompt \"{prompt_str}\": ").strip() or prompt_str

conversation_history: list = [{"role": "system", "content": system_str}] # Initialize conversation history

def chat_with_model(prompt: str) -> None:
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
        print()

        # Combine all chunks into a single response
        full_response = ''.join(response_chunks)
        conversation_history.append({"role": "assistant", "content": full_response})

#        # print conversation diagnositcs
#        for item in conversation_history:
#            print(Fore.YELLOW + f"{item.get("role")}: {item.get("content")}")
#            #print(list(item.items()))

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