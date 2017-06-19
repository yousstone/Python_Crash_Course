#!/usr/bin/python
# coding=utf8

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(size='Large',msg='I Love Python'):
	print('''\nThe size of T-Shirt is %s 
and a message that will be printed on is "%s"''') % (size,msg)

make_shirt()

make_shirt(size='Small')
