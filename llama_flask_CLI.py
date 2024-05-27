import requests
import readline
from datetime import datetime

def main():
    base_url = 'http://127.0.0.1:5000/chat'  # The URL for the Flask backend chat endpoint

    print("Welcome to the llama chatbot CLI")
    print("Type your command or type 'quit' to exit.")

    # Enable readline to handle command history
    readline.parse_and_bind("tab: complete")  # Enable tab completion for command history
    readline.parse_and_bind("set editing-mode vi")  # Optional: set vi or emacs editing mode

    # Optionally load command history from a file
    history_file = ".cli_client_history"
    try:
        readline.read_history_file(history_file)
    except FileNotFoundError:
        pass  # If the history file doesn't exist, continue without error

    while True:
        try:
            # Get user input with history support
            user_input = input("Ask llama chatbot (or 'quit' to exit): ")

            if user_input.lower() == "quit":
                print("Exiting the CLI. Goodbye!")
                break  # Exit the loop and end the program

            # Check if the input is empty or whitespace
            if not user_input.strip():
                print("Input cannot be empty or whitespace. Please enter a valid prompt.")
                continue  # Skip to the next iteration of the loop

            # Prepare the payload for the POST request
            payload = {'prompt': user_input}

            # Print timestamp before sending the request
            start_time = datetime.now()
            print(f"Sending request at: {start_time}")

            # Send the POST request to the Flask backend
            response = requests.post(base_url, json=payload)

            # Print timestamp after receiving the response
            end_time = datetime.now()
            print(f"Received response at: {end_time}")

            # Check if the request was successful
            if response.status_code == 200:
                # Extract the chatbot's response from the JSON
                reply = response.json().get('response', '')
                print(f"Chatbot: {reply} \n")
            else:
                # Print error message if the request failed
                print(f"Error: {response.status_code} - {response.text}")

            # Save command history after each input
            readline.write_history_file(history_file)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break  # Handle Ctrl+C gracefully and exit the loop
        except Exception as e:
            # Print any other exceptions that occur
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
