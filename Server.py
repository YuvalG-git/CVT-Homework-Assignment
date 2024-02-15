from flask import Flask, render_template
from flask_socketio import SocketIO, send
import messageHistoryHandler

app = Flask(__name__)
# does not work without cors_allowed_origins="*"
socket = SocketIO(app, cors_allowed_origins="*")


# The function is used as a route to serve the client's HTML page
@app.route('/')
def chat():
    return render_template('chat.html')


# The function indicates that a client has logged in
@socket.event
def connect():
    print('Client connected')


# The function indicates that a client has logged out
@socket.event
def disconnect():
    print('Client disconnected')


# The function receives the username socket id
# It sends the message history to a client on login
@socket.event
def message_history_request(sid):
    socket.emit('message_history', messageHistoryHandler.message_history, room=sid)


# The function receives a dictionary containing the message details - sender name, message content and time
# The function handle the process of receiving messages: it shows the message content and send it to all connected users
# except for the one who sent the message
@socket.event
def handle_message(message_data):
    try:
        sender = message_data['sender']
        message = message_data['message']
        time = message_data['time']

        print('Received message from {}: {}'.format(sender, message))
        send({'sender': sender, 'message': message, 'time': time}, broadcast=True, include_self=False)
        messageHistoryHandler.message_history.append({'sender': sender, 'message': message, 'time': time})
    except AssertionError as e:
        print("AssertionError occurred:", e)
    # instead of using the following code after each message,
    # the whole message history is inserted to the JSON file on server disconnect
    # I acknowledge the problem that might happen on a server exception...
    # a good solution might be saving to the JSON file after a certain number of received messages
    # because it's a small project I chose not to handle it...
    # with open('messages.json', 'w') as file:
    #    json.dump(message_history, file, indent=4)


if __name__ == '__main__':
    socket.run(app, allow_unsafe_werkzeug=True)
