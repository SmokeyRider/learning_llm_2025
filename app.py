from flask import Flask, render_template, request, redirect, url_for
from ollama import list as ollama_list, chat as ollama_chat  # Import specific functions

app = Flask(__name__)

# Set default values
DEFAULT_MODEL = "llama3.2"
DEFAULT_SYSTEM_PROMPT = "You are Odin's helpful assistant."
DEFAULT_PROMPT = "I am Odin, the All-Father. Where do I live?"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_STREAMING = True
MAX_TEMP = 0.9
MIN_TEMP = 0.1
MIN_TEMP_STEP = 0.1

# Initialize variables with default values
model_name = DEFAULT_MODEL
system_prompt = DEFAULT_SYSTEM_PROMPT
user_prompt = DEFAULT_PROMPT
model_temperature = DEFAULT_TEMPERATURE
streaming_output = DEFAULT_STREAMING
model_names = []

# Get list of available models
try:
    model_set = ollama_list()
    for model in model_set.models:
        model_names.append(model.model)
    model_names.sort()
except Exception as e:
    print("An error occurred listing Ollama models:", str(e))
    exit(1)

conversation_history = [{"role": "system", "content": system_prompt}]

@app.route('/', methods=['GET', 'POST'])
def index():
    global user_prompt, conversation_history, model_name, system_prompt, model_temperature
    if request.method == 'POST':
        user_prompt = request.form['prompt']
        model_name = request.form['model']
        system_prompt = request.form['system_prompt']
        model_temperature = float(request.form['model_temperature'])
        conversation_history.append({"role": "user", "content": user_prompt})
        print(f'model temperature: {model_temperature}')
        response = ollama_chat(
            model=model_name,
            messages=conversation_history,
            stream=streaming_output,
            options={'temperature': model_temperature}
        )
        response_chunks = []
        for chunk in response:
            chunk_content = chunk['message']['content']
            response_chunks.append(chunk_content)
        full_response = ''.join(response_chunks)
        conversation_history.append({"role": "assistant", "content": full_response})
    else:   
        user_prompt = ''
        full_response = ''
    return render_template('index.html', prompt=user_prompt, response=full_response, models=model_names, selected_model=model_name, system_prompt=system_prompt, model_temperature=model_temperature, min_temp=MIN_TEMP, max_temp=MAX_TEMP, min_temp_step=MIN_TEMP_STEP)

if __name__ == '__main__':
    app.run(debug=True)