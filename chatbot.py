from flask import Flask, render_template, request, redirect, url_for
from ollama import list as ollama_list, chat as ollama_chat  # Import specific functions
import markdown

app = Flask(__name__)

# Set default values
DEFAULT_MODEL:str = "llama3.2:latest"
DEFAULT_SYSTEM_PROMPT:str = "You are Odin's helpful assistant."
DEFAULT_PROMPT:str = "Tell me a joke"
DEFAULT_TEMPERATURE:float = 0.7
DEFAULT_STREAMING:float = True
MAX_TEMP:float = 0.9
MIN_TEMP:float = 0.1
MIN_TEMP_STEP:float = 0.1

# Initialize variables with default values
model_name:str = DEFAULT_MODEL
system_prompt:str = DEFAULT_SYSTEM_PROMPT
user_prompt:str = DEFAULT_PROMPT
model_temperature:float = DEFAULT_TEMPERATURE
streaming_output = DEFAULT_STREAMING
model_names:list = []
response_history:str = ''

# Get list of available models
try:
    model_set = ollama_list()
    for model in model_set.models:
        model_names.append(model.model)
    model_names.sort()
except Exception as e:
    print("An error occurred listing Ollama models:", str(e))
    exit(1)

@app.route('/', methods=['GET', 'POST'])
def index():
    global user_prompt, conversation_history, model_name, system_prompt, model_temperature, response_history
    if request.method == 'POST':
        user_prompt = request.form['prompt']
        model_name = request.form['model']
        system_prompt = request.form['system_prompt']
        model_temperature = float(request.form['model_temperature'])
        conversation_history = [msg for msg in conversation_history if msg["role"] != "system"] # clear assistant messages from history
        conversation_history.append({"role": "system", "content": system_prompt})
        conversation_history.append({"role": "user", "content": user_prompt})
        print(f'model name: {model_name}')
        print(f'model temperature: {model_temperature}')
        print(f'system prompt: {system_prompt}')
        print(f'user prompt: {user_prompt}')
        response = ollama_chat(
            model=model_name,
            messages=conversation_history,
            stream=streaming_output,
            options={'temperature': model_temperature}
        )
        print(f'Response: ',end='')
        response_chunks = []
        for chunk in response:
            chunk_content = chunk['message']['content']
            response_chunks.append(chunk_content)
            print(f'{chunk_content}', end='', flush=True)
        print('')
        full_response = ''.join(response_chunks)
        conversation_history.append({"role": "assistant", "content": full_response})

        # Convert markdown to HTML
        full_response = markdown.markdown(full_response)

        #full_response = full_response.replace('\n', '\n<br>') #add HTML line breaks to the response
        full_response = full_response.replace('<think>', '<div class="chat-message thinking">Thinking... ')
        full_response = full_response.replace('</think>', '</div>')
        response_history += f'<div class="chat-message user">{user_prompt}</div><div class="chat-message assistant">{full_response}</div>'

        user_prompt = '' #clear the user prompt after 
        # print debugging info
        print(f'DIAG: conversation history: {len(conversation_history)}')
        for message in conversation_history:
            print(f"DIAG: {message}")

    else:   # GET request
        response_history = ''
        conversation_history = []
    return render_template('index.html', prompt=user_prompt, response=response_history, models=model_names, selected_model=model_name, system_prompt=system_prompt, model_temperature=model_temperature, min_temp=MIN_TEMP, max_temp=MAX_TEMP, min_temp_step=MIN_TEMP_STEP)

if __name__ == '__main__':
    app.run(debug=True)