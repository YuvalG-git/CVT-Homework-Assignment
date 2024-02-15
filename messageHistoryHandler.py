import json
import os
import signal
import sys


# the function load the messages from the JSON file and returns them
def load_messages():
    if os.path.exists(json_file_name):
        with open(json_file_name, 'r') as file:
            return json.load(file)
    else:
        return []


# this signal handler function saves messages to the JSON file before it shut down
def save_messages_before_shut_down(signal, frame):
    print("Server is shutting down. Saving messages...")
    with open(json_file_name, 'w') as file:
        json.dump(message_history, file, indent=4)
    sys.exit(0)


json_file_name = 'messages.json'

# message_history saves the message history
# when the server is up, it loads all the messages from the JSON file
message_history = load_messages()

# those code lines register the signal handler:
# Handles Ctrl+C scenario
signal.signal(signal.SIGINT, save_messages_before_shut_down)
# Handles termination signal scenario
signal.signal(signal.SIGTERM, save_messages_before_shut_down)