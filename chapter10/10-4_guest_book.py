#!/usr/bin/python3
# coding=utf8

'''
10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
'''
print('\nIf you want to quit,please enter "quit"')
active = True
file_name = 'guest_book.txt'
while active:
    user_name = input('Please enter your name : ')
    if user_name == 'quit':
        active = False
        print('-'*20 + 'Bye-Bye' + '-'*20)
    else:
        with open(file_name,'a') as file_object:
            greet_str = 'Hello ' + user_name +' welcome you!\n'
            print(greet_str+'\n')
            file_object.write(greet_str)
