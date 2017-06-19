#!/usr/bin/python
# coding=utf8

'''
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.

'''
glossary = {
	'variable':'A variable is a value that can change, depending on conditions or on information passed to the program.',
	'tuple':'A tuple is a sequence of immutable Python objects',
	'list':'The most basic data structure in Python is the sequence. Each element of a sequence is assigned a number - its position or index. The first index is zero, the second index is one, and so forth.',
	'dictionary':'A dictionary is an associative array (also known as hashes)',
	'functions':'A function is a block of organized, reusable code that is used to perform a single, related action'
}

for key ,value in glossary.items():
	print('\n%s means : %s'%(key,value))