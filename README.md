# This program runs on Macbook (apple silicon)
    Model runs on CPU, so reply is slow (around 4min).

# Install brew
    $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Download llama model
    $ brew install git-lfs
    $ git lfs install
    $ git clone https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct

## Meta-Llama-3-8B-Instruct should be located in parallel with python code folder
    tree
    .
    ├── Meta-Llama-3-8B-Instruct
    │   ├── LICENSE
    │   ├── README.md
    │   ├── USE_POLICY.md
    │   ├── config.json
    │   ├── generation_config.json
    │   ├── model-00001-of-00004.safetensors
    │   ├── model-00002-of-00004.safetensors
    │   ├── model-00003-of-00004.safetensors
    │   ├── model-00004-of-00004.safetensors
    │   ├── model.safetensors.index.json
    │   ├── original
    │   │   ├── consolidated.00.pth
    │   │   ├── params.json
    │   │   └── tokenizer.model
    │   ├── special_tokens_map.json
    │   ├── tokenizer.json
    │   └── tokenizer_config.json
    └── simple_llama
        ├── README.md
        ├── llama_flask_CLI.py
        └── llama_flask_backend.py

# PIP install [Macbook]
    $ pip3 install transformers torch
    $ pip3 install sentencepiece
    $ pip3 install --upgrade transformers sentencepiece

# Start the Flask backend
    python3 llama_flask_backend.py
    Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.
    Loading checkpoint shards: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:08<00:00,  2.19s/it]
    Chatbot is ready!
    * Serving Flask app 'llama_flask_backend'
    * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit

# Start CLI
    python3 llama_flask_CLI.py
    Welcome to the llama chatbot CLI
    Type your command or type 'quit' to exit.
    Ask llama chatbot (or 'quit' to exit):

# CLI reply example
    python3 llama_flask_CLI.py
    Welcome to the llama chatbot CLI
    Type your command or type 'quit' to exit.
    Ask llama chatbot (or 'quit' to exit):
    Input cannot be empty or whitespace. Please enter a valid prompt.
    Ask llama chatbot (or 'quit' to exit): what is NBA?
    Sending request at: 2024-05-26 22:29:19.301633
    Received response at: 2024-05-26 22:32:48.866152
    Chatbot: what is NBA? NBA stands for National Basketball Association. It is a professional basketball league in North America, comprising 30 teams from the United States and Canada. The NBA is considered the premier men's professional basketball league in the world and is one of the four major professional sports leagues in North America, along with the National Football League (NFL), Major League Baseball (MLB), and the National Hockey League (NHL). The league was founded in 1946 and has been growing in popularity ever since. The NBA

    Ask llama chatbot (or 'quit' to exit):
