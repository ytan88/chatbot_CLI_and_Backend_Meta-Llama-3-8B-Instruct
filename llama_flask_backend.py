from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

# Create a Flask application instance
app = Flask(__name__)

# Path to the local model directory
local_model_path = "../Meta-Llama-3-8B-Instruct"

# Function to load the tokenizer from the specified model path
def load_tokenizer(model_path):
    try:
        # Attempt to load the tokenizer using the Hugging Face AutoTokenizer class
        tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=True)
        return tokenizer
    except Exception as e:
        # Print an error message if loading fails and return None
        print(f"Error loading tokenizer: {e}")
        return None

# Function to load the model from the specified model path
def load_model(model_path):
    try:
        # Attempt to load the model using the Hugging Face AutoModelForCausalLM class
        # The model is loaded with bfloat16 precision to save memory
        model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.bfloat16)
        return model
    except Exception as e:
        # Print an error message if loading fails and return None
        print(f"Error loading model: {e}")
        return None

# Function to set up the text generation pipeline
def setup_pipeline(model, tokenizer):
    try:
        # Create a text-generation pipeline using the loaded model and tokenizer
        text_generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
        return text_generator
    except Exception as e:
        # Print an error message if setting up the pipeline fails and return None
        print(f"Error setting up pipeline: {e}")
        return None

# Function to initialize the model, tokenizer, and pipeline
def initialize():
    global text_generator

    # Load the tokenizer
    tokenizer = load_tokenizer(local_model_path)
    if not tokenizer:
        print("Failed to load tokenizer. Exiting.")
        return

    # Load the model
    model = load_model(local_model_path)
    if not model:
        print("Failed to load model. Exiting.")
        return

    # Set up the text generation pipeline
    text_generator = setup_pipeline(model, tokenizer)
    if not text_generator:
        print("Failed to set up pipeline. Exiting.")
        return

    print("Chatbot is ready!")

# Define a route for generating text using the chatbot
@app.route('/chat', methods=['POST'])
def generate_text():
    # Get the JSON data from the request
    data = request.json
    # Extract the 'prompt' field from the JSON data
    input_prompt = data.get('prompt', '')
    # If no prompt is provided, return an error response
    if not input_prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    try:
        # Generate text using the text generation pipeline
        generated_text = text_generator(input_prompt, max_new_tokens=100, do_sample=True, temperature=0.7)
        # Return the generated text as a JSON response
        return jsonify({'response': generated_text[0]['generated_text']})
    except Exception as e:
        # Return an error response if text generation fails
        return jsonify({'error': str(e)}), 500

# Main entry point of the script
if __name__ == '__main__':
    # Initialize the model, tokenizer, and pipeline
    initialize()
    # Run the Flask app on localhost at port 5000
    app.run(host='127.0.0.1', port=5000)
