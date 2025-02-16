from flask import Flask, request, jsonify, render_template
from ollama import list as ollama_list, chat as ollama_chat

# Initialize Flask app
app = Flask(__name__)

# Get list of available models
try:
    model_set = ollama_list()
except Exception as e:
    print("An error occurred listing Ollama models:", str(e))
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

# Define routes
@app.route('/')
def index():
    return render_template('index.html', models=model_names)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['prompt']
    response = chat_with_model(user_input)
    return jsonify({"response": response})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)