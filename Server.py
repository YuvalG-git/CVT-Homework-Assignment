from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socket = SocketIO(app)


# The method indicates that a client has logged in
@socket.event
def connect():
    print('Client connected')


# The method indicates that a client has logged out
@socket.event
def disconnect():
    print('Client disconnected')


# The method handle the process of receiving messages: it shows the message content and send it to all connected users
@socket.event
def handle_message(message):
    print('Received message:', message)
    socket.emit('receive_message', message)


if __name__ == '__main__':
    socket.run(app, host='localhost', port=5000, allow_unsafe_werkzeug=True)
