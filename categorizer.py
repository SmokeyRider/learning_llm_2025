import ollama
import os

model_name = "deepseek-r1" # Specify the model to use

input_file = "./data/grocery_list.txt"
output_file = "./data/categorized_grocery_list.txt"

if not os.path.exists(input_file):
    print(f"Input file {input_file} does not exist.")
    exit(1)

with open(input_file, "r") as file_in:
    items = file_in.read().strip()

# Prepare the prompt for the model
prompt = f"""
You are an assistant that categorizes and sorts grocery items.

Here is a list of grocery items:

{items}

Please:

1. Categorize these items into appropriate grocery store departments such as Produce, Dairy, Meat, Beverages, etc.
2. Sort the items alphabetically within each category.
3. Present the categorized list in a clear and organized manner, using bullet points or numbering.
4. Do not list any items more than once in the output list.

"""

try:
    response = ollama.generate(model=model_name, prompt=prompt, )
    generateed_text = response.get("response", "")
    print(generateed_text.strip())

    with open(output_file, "w") as file_out:
        file_out.write(generateed_text.strip())    

    print(f"Categorized grocery list saved to {output_file}")
except Exception as e:
    print("An error occurred: ", str(e))