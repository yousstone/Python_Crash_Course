#!/usr/bin/python
# coding=utf8

'''
10-2. Learning C: You can use the replace() method to replace any word in a
string with a different word. Here’s a quick example showing how to replace
'dog' with 'cat' in a sentence:
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen.

'''

file_name = 'learning_python.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()

# learning_c = []
for line in lines:
    # learning_c.append(line.replace('python','C'))
    print(line.replace('python','C').strip())
    # print(line)
