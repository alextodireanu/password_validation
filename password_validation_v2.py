# second method using re module

import re
user_password = input('Type your password here -> ')

def evaluate_password(password):
    """Method to check if the password matches our criteria using the re module"""
    if len(password) < 7:
        print('Weak')
        return

    # converted 2 regex patterns in regex objects that can be searched in the user's input
    # the patterns are as follows:
    # any of the special characters repeated at least 2 times with any number of characters between them
    # any number between 0-9 repeated at least 2 times with any number of characters between them
    special_characters = re.compile(r'[!@#$%&*](.*){2,}')
    numbers = re.compile(r'[0-9](.*){2,}')

    # searching for our patterns in the user's input 
    special_characters = special_characters.search(password)
    numbers = numbers.search(password)

    if special_characters and numbers:
        print('Strong')
    else:
        print('Weak')



