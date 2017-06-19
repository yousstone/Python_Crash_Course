#!/usr/bin/python3
# coding=utf8

'''
10-3. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
'''

file_name = 'guest.txt'
user_name = input('Please enter your name: ')
with open(file_name,'a') as file_object:
    file_object.write(user_name+'\n')

