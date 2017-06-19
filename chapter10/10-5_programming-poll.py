#!/usr/bin/python3
# coding=utf8

'''
10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
'''

print('\nIf you want to quit,please enter "quit"')
active = True
file_name = 'Programming_poll.txt'
while active:
    reason = input('\nPlease tell me why do you like programming?  \n')
    if reason == 'quit':
        active = False
        print('-'*20 + 'Bye-Bye' + '-'*20)
    else:
        with open(file_name,'a') as file_object:
            file_object.write(reason+'\n')
