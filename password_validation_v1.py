# You're interviewing to join a security team. They want to see you build a password evaluator for your technical
# interview to validate the input.

# Task: Write a program that takes in a string as input and evaluates it as a valid password. The password is valid
# if it has at a minimum 2 numbers, 2 of the following special characters ('!', '@', '#', '$', '%', '&', '*'), and a
# length of at least 7 characters. If the password passes the check, output 'Strong', else output 'Weak'.

# Input: a string representing the password to evaluate.

# first method using a for loop and linear search
def evaluate_password(password):
    """Method to check if the password matches our criteria"""

    if len(password) < 7:
        print('Weak')
        return

    special_characters = ('!', '@', '#', '$', '%', '&', '*')
    numbers_count = 0
    special_characters_count = 0

    for character in password:
        if character.isdigit():
            numbers_count += 1
        else:
            if character in special_characters:
                special_characters_count += 1

    if numbers_count >= 2 and special_characters_count >= 2:
        print('Strong')
    else:
        print('Weak')


user_password = input('Type your password here -> ')
evaluate_password(user_password)
