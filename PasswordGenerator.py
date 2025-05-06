import random

number_list = [1,2,3,4,5,6,7,8,9,10,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

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
