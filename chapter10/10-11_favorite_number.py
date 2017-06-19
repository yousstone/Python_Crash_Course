#!/usr/bin/python3
# coding=utf8
'''
10-11. Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate program
that reads in this value and prints the message, “I know your favorite
number! It’s _____.”
'''
import json
filename = 'favorite_number.json'
num = input('Please enter your favorite number : ')
with open(filename,'w') as f_obj:
    json.dump(num,f_obj)

with open(filename) as f_obj:
    num = json.load(f_obj)

print("I know your favorite number! It's %d" % int(num))