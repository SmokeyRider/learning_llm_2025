import tkinter as tk
from tkinter import scrolledtext
from ollama import list as ollama_list, chat as ollama_chat
from colorama import init, Fore

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
for model in model_set.models:
    model_name = model.model.split(":")[0]
    model_names.append(model_name)

# Set default values
model_str = "llama3.2"
system_str = "You are Odin's helpful assistant."
conversation_history = [{"role": "system", "content": system_str}]

# Function to chat with the model
def chat_with_model(prompt):
    try:
        conversation_history.append({"role": "user", "content": prompt})
        response = ollama_chat(model=model_str, messages=conversation_history, stream=True)
        
        response_chunks = []
        for chunk in response:
            chunk_content = chunk['message']['content']
            response_chunks.append(chunk_content)
        
        full_response = ''.join(response_chunks)
        conversation_history.append({"role": "assistant", "content": full_response})
        return full_response
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Function to handle sending messages
def send_message():
    user_input = user_entry.get()
    if user_input.strip() == "":
        return
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"You: {user_input}\n")
    chat_history.config(state=tk.DISABLED)
    chat_history.yview(tk.END)
    user_entry.delete(0, tk.END)
    
    response = chat_with_model(user_input)
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"Assistant: {response}\n")
    chat_history.config(state=tk.DISABLED)
    chat_history.yview(tk.END)

# Create the main application window
root = tk.Tk()
root.title("Odin Chat Assistant")

# Create a scrolled text widget for the chat history
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create an entry widget for user input
user_entry = tk.Entry(root, width=100)
user_entry.pack(padx=10, pady=10, fill=tk.X, expand=True)
user_entry.bind("<Return>", lambda event: send_message())

# Create a button to send the message
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10)

# Start the main loop
root.mainloop()