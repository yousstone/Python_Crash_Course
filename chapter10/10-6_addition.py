#!/usr/bin/python3
# coding=utf8

'''
10-6. Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you’ll get a TypeError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the TypeError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.
'''

try:

    a = input('Please enter an number for a: ')
    a = int(a)

    b = input('Please enter an number for b: ')
    b = int(b)

except ValueError:
    print('Sorry, I need a number not a string. ')

else:
    sum = a + b
    print('a + b = %s'%str(sum))