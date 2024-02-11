import socketio
import asyncio


async def main():
    try:
        # create an asynchronous socket
        socket = socketio.AsyncClient()

        # The method indicates that the client logged in
        @socket.event
        async def connect():
            print("The client has been successfully connected to the server")

        # The method indicates that the client logged out
        @socket.event
        async def disconnect():
            print("The Client has disconnected from the server")

        # The method handles the received message
        @socket.event
        async def receive_message(data):
            print('Received message:', data)

        await socket.connect('http://localhost:5000')

        # send a message to the server
        await socket.emit('handle_message', 'Hello from {0}'.format(user_name))

        await socket.wait()

    except Exception as e:
        print(f"An error occurred: {e}")

# handle the name selection and start the connection to the server
if __name__ == '__main__':
    user_name = input("Enter name: ")
    asyncio.run(main())




