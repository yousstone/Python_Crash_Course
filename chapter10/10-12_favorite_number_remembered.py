#!/usr/bin/python3
# coding=utf8
'''
10-12. Favorite Number Remembered: Combine the two programs from
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works.
'''
import json
filename = 'favorite_number.json'
try:
    with open(filename) as f_obj:
        num = json.load(f_obj)
except FileNotFoundError:
    num = input('Please enter your favorite number : ')
    with open(filename, 'w') as f_obj:
        json.dump(num, f_obj)
else:
    print("I know your favorite number! It's %d" % int(num))