#!/usr/bin/python
# coding=utf8

'''
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.

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

glossary['loop'] = 'loop is ......'
glossary['if'] = 'if is .....'
glossary['while'] = 'while is .....'
glossary['break'] = 'break is .....'
glossary['continue'] = 'continue is .....'

for key ,value in glossary.items():
	print('\n%s means : %s'%(key,value))