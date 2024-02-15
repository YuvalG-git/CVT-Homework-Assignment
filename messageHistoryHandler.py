import json
import os
import signal
import sys

json_file_name = 'messages.json'


# The function loads the messages from the JSON file and returns them
def load_messages(json_file=json_file_name):
    if os.path.exists(json_file):
        with open(json_file, 'r') as file:
            return json.load(file)
    else:
        return []


# message_history saves the message history
# when the server is up, it loads all the messages from the JSON file
message_history = load_messages()


# This signal handler function saves messages to the JSON file before it shut down
def save_messages_before_shut_down(signal, frame, json_file=json_file_name):
    print("Server is shutting down. Saving messages...")
    save_messages(json_file)
    sys.exit(0)


# The function saves messages to the JSON file
def save_messages(json_file=json_file_name, history=message_history):
    with open(json_file, 'w') as file:
        json.dump(history, file, indent=4)


# those code lines register the signal handler:
# Handles Ctrl+C scenario
signal.signal(signal.SIGINT, save_messages_before_shut_down)
# Handles termination signal scenario
signal.signal(signal.SIGTERM, save_messages_before_shut_down)