#!/usr/bin/python
# coding=utf8

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

def make_shirt(size,msg):
	print('''\nThe size of T-Shirt is %s 
and a message that will be printed on is "%s"''') % (size,msg)

make_shirt('M','Life is short, i use python.')

make_shirt(size='L',msg='Just do it')
