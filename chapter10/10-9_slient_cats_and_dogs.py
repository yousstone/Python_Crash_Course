#!/usr/bin/python3
# coding=utf8

'''
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
silently if either file is missing.
'''

file_pets = ['cats.txt','dogs.txt']


for file_name in file_pets:
    try:
        with open(file_name) as f_object:
            content = f_object.read()
            print(content)
    except FileNotFoundError:
        pass
