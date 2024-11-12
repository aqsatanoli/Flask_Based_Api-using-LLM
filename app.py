import os
from flask import Flask, request, jsonify
import replicate

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1> Welcome to ROBX.AI Intership Task 1 </h1>"

@app.route('/generate_Text', methods=['POST'])
def generate_text():
    data = request.get_json()
    
    if not data or "prompt" not in data:
        return jsonify({"error": "Invalid JSON or 'prompt' key not provided"}), 400

    prompt = data.get("prompt")
    response = {
        "prompt": prompt,
        "max_new_tokens": 512,
        "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
    }

    try:
        # Initialize the Replicate client with the API key
        client = replicate.Client(api_token="r8_1oZGFvx7JFfo400P29PyFVy6FXT1N6c1mdJgy")  # Replace with actual API key
        output = client.run("meta/meta-llama-3-8b-instruct", input=response)
        output_text = "".join(output)  # Properly join output if it's a list of strings
        return jsonify({"response": output_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
