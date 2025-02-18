from ollama import list as ollama_list, chat as ollama_chat  # Import specific functions
from colorama import init, Fore, Style

# Set default values
DEFAULT_MODEL: str = "llama3.2"
DEFAULT_SYSTEM_PROMPT: str = "You are Odin's helpful assistant."
DEFAULT_PROMPT: str = "I am Odin, the All-Father.  Where do I live?"
DEFAULT_TEMPERATURE: float = 0.7
DEFAULT_STREAMING: bool = True
MINIMUM_TEMPERATURE: int = 0.0
MAXIMUM_TEMPERATURE: int = 1.0

# Initialize variables with default values
model_name: str = DEFAULT_MODEL
system_prompt: str = DEFAULT_SYSTEM_PROMPT
user_prompt: str = DEFAULT_PROMPT
model_temperature: float = DEFAULT_TEMPERATURE
streaming_output: bool = DEFAULT_STREAMING
model_names: list[str] = [] #empty list to store model names

# Initialize colorama
init(autoreset=True)

# Get list of available models
try:
    model_set = ollama_list()
except Exception as e:
    print(Fore.RED + "An error occurred listing Ollama models:", str(e))
    exit(1)

# Iterate over the list and populate a list of model names
print(Fore.GREEN + "Available model names: ")
for model in model_set.models:
    model_names.append(model.model)  # Append the processed model name to the list

model_names.sort()  # Sort the list of model names alphabetically

# Print the list of model names
for name in model_names:
    print(Fore.GREEN + f"\t{name}", flush=True)

# Prompt model overrides
while True:
    model_name = input(f"Model Name \"{model_name}\": ") or model_name
    if  ":" not in model_name: # add ":latest" if not specified
        model_name = model_name + ":latest"
    if model_name.lower() in (name.lower() for name in model_names):
        break
    else:
        print(Fore.RED + f"Model Name \"{model_name}\" Not valid. Please try again.")
        print(Fore.GREEN + "Available models: ")
        for name in model_names:
            print(Fore.GREEN + f"\t{name}", flush=True)

# Prompt for temperature overrides with validation
while True:
    model_temperature = float(input(f"Model Temperature \"{model_temperature}\": ") or model_temperature)
    if MINIMUM_TEMPERATURE <= model_temperature <= MAXIMUM_TEMPERATURE:
        break
    else:
        print(Fore.RED + f"Model Temperature {model_temperature} must be between {MINIMUM_TEMPERATURE} and {MAXIMUM_TEMPERATURE}. Please try again.")

# prompt for system string overrides
system_prompt = input(f"System Prompt \"{system_prompt}\": ").strip() or system_prompt

# Prompt for prompt overrides
user_prompt = input(f"User Prompt \"{user_prompt}\": ").strip() or user_prompt

conversation_history: list = [{"role": "system", "content": system_prompt}] # Initialize conversation history

def chat_with_model(prompt: str) -> None:
    """
    Function to chat with the model.
    """
    try:
        conversation_history.append({"role": "user", "content": prompt})
        response = ollama_chat(
            model=model_name,
            messages=conversation_history,
            stream=streaming_output,
            options={'temperature': model_temperature} # very conservative (good for coding and correct syntax)
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
    chat_with_model(user_prompt)
    user_prompt = input("\n\nUser Prompt: ").strip()
    if user_prompt.lower() in ["exit", "quit", ""]:
        break
exit(0)