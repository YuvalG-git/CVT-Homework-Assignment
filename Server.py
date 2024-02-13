from flask import Flask, render_template
from flask_socketio import SocketIO, send
import json
import os
import signal
import sys

app = Flask(__name__)
# does not work without cors_allowed_origins="*"
socket = SocketIO(app, cors_allowed_origins="*")


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


# The function use as a route to serve the client's HTML page
@app.route('/')
def chat():
    return render_template('chat.html')


# The function indicates that a client has logged in
@socket.event
def connect():
    print('Client connected')


# The function sends the message history to a client on login
@socket.event
def message_history_request():
    socket.emit('message_history', message_history)


# The function indicates that a client has logged out
@socket.event
def disconnect():
    print('Client disconnected')


# The function handle the process of receiving messages: it shows the message content and send it to all connected users
# except for the one who sent the message
@socket.event
def handle_message(message):
    print('Received message:', message)
    try:
        send(message, broadcast=True, include_self=False)
    except AssertionError as e:
        print("AssertionError occurred:", e)
    message_history.append({"content": message})

    # instead of using the following code after each message,
    # the whole message history is inserted to the JSON file on server disconnect
    # I acknowledge the problem that might happen on a server exception...
    # a good solution might be saving to the JSON file after a certain number of received messages
    # because it's a small project I chose not to handle it...
    # with open('messages.json', 'w') as file:
    #    json.dump(message_history, file, indent=4)


json_file_name = 'messages.json'

# message_history saves the message history
# when the server is up, it loads all the messages from the JSON file
message_history = load_messages()

# those code lines register the signal handler:
# Handles Ctrl+C scenario
signal.signal(signal.SIGINT, save_messages_before_shut_down)
# Handles termination signal scenario
signal.signal(signal.SIGTERM, save_messages_before_shut_down)

if __name__ == '__main__':
    socket.run(app, allow_unsafe_werkzeug=True)
