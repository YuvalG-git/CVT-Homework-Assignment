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


# The function returns True if the list is empty
# Else, it returns False
def is_list_empty(list_value):
    if not list_value:
        return True
    else:
        return False


# The method prints the test result
def print_test_result(test_name, test_result):
    if test_result is True:
        success_value = "pass"
    else:
        success_value = "fail"
    print("[{}] result is: {}".format(test_name, success_value), end="\n\n")

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

# checks the scenario when loading from non-existing file
file_not_exist_history = messageHistoryHandler.load_messages("NotExist.json")
print_test_result("File Not Exist", is_list_empty(file_not_exist_history))

# clears the JSON file from past content
clear_file(json_file_name)

# checks the scenario when loading from an empty file
empty_message_history = messageHistoryHandler.load_messages(json_file_name)
print_test_result("Empty File", is_list_empty(empty_message_history))

# creates a list of the checked messages
messages = [message_data_1, message_data_2, message_data_3, message_data_4]

# saves the messages to 'Test.json' file
messageHistoryHandler.save_messages(json_file_name, messages)

# loads the messages from the 'Test.json' file
message_history = messageHistoryHandler.load_messages(json_file_name)

message_was_not_different = True

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
        message_was_not_different = False
    print(message, end="\n\n")
print_test_result("File With Values - Same Values", message_was_not_different)

# checks if the lists' length is identical
message_length = len(messages)
message_history_length = len(message_history)
print_test_result("File With Values - Values Number", message_length == message_history_length)


