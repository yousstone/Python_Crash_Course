#!/usr/bin/python
# coding=utf8
'''
9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
used a standard dictionary to represent a glossary. Rewrite the program using
the OrderedDict class and make sure the order of the output matches the order
in which key-value pairs were added to the dictionary.
'''
from collections import OrderedDict

glossary = OrderedDict()

glossary['loop'] = 'loop is ......'
glossary['if'] = 'if is .....'
glossary['while'] = 'while is .....'
glossary['break'] = 'break is .....'
glossary['continue'] = 'continue is .....'

for key ,value in glossary.items():
	print('\n%s means : %s'%(key,value))