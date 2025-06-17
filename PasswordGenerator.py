import random
import string 

number_list = (string.ascii_letters + string.digits + string.punctuation)

def user_choice():
    user_input = input('Welcome to the password generator! Pick a password length: \n 1. 8 characters \n 2. 12 characters \n 3. 16 characters\n')

    if user_input == '1':
        print(*random.sample(number_list, 8))
    elif user_input == '2':
        print(*random.sample(number_list, 12))
    elif user_input == '3':
        print(*random.sample(number_list, 16))
    else:
        print('Choose 1-3 only!')

user_choice()
