import messageHistoryHandler
import string

# create a string of the alphabet lowercase letters times 1000
alphabet = string.ascii_lowercase
long_string = alphabet * 1000

json_file_name = 'Test.json'


# The function clear the JSON file data
def clear_file(json_file):
    with open(json_file, 'w') as file:
        file.write('[]')


# The function prints if the list is empty or not
def handle_empty_list(list_value):
    if not list_value:
        print("the list is empty", end="\n\n")
    else:
        print("the list is not empty", end="\n\n")


# unit test code:

# checks regular string
message_data_1 = {
    'sender': 'Yuval',
    'message': 'Hello, Tamar!',
    'time': '15/02/24 12:00:00'
}

# checks empty string
message_data_2 = {
    'sender': '',
    'message': '',
    'time': ''
}

# checks long string
message_data_3 = {
    'sender': long_string,
    'message': long_string,
    'time': long_string
}

# checks '}'
message_data_4 = {
    'sender': "}",
    'message': "}",
    'time': "}"
}

# checks the scenario when loading from non-exist file
file_not_exist_history = messageHistoryHandler.load_messages("NotExist.json")
handle_empty_list(file_not_exist_history)

# clears the JSON file from past content
clear_file(json_file_name)

# checks the scenario when loading from an empty file
empty_message_history = messageHistoryHandler.load_messages(json_file_name)
handle_empty_list(empty_message_history)

# creates a list of the checked messages
messages = [message_data_1, message_data_2, message_data_3, message_data_4]

# saves the messages to 'Test.json' file
messageHistoryHandler.save_messages(json_file_name, messages)

# loads the messages from the 'Test.json' file
message_history = messageHistoryHandler.load_messages(json_file_name)


message_was_different = False

# for each message, it prints the message content and the process success
for message in message_history:
    if message == message_data_1:
        print("Message is identical to message_data_1:")
    elif message == message_data_2:
        print("Message is identical to message_data_2:")
    elif message == message_data_3:
        print("Message is identical to message_data_3:")
    elif message == message_data_4:
        print("Message is identical to message_data_4:")
    else:
        print("Message is different:")
        message_was_different = True
    print(message, end="\n\n")

if message_was_different is False:
    print("WORKS!", end="\n\n")

# checks if the lists' length is identical
message_length = len(messages)
message_history_length = len(message_history)
if message_length == message_history_length:
    print("Same number: {}\nworked! :)".format(message_length), end="\n\n")
else:
    print("different number :(", end="\n\n")

