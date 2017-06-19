#!/usr/bin/python
# coding=utf8


# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.

def favorite_book(name='Kobe',title):
	print("""One of %s's favourite book is %s""") % (name,title)

# multiple function calls

# positional argument
favorite_book('Python Crash Couser','Tesla')
# keyword argument
favorite_book(title = 'Python Crash Couser',name='Tesla')
# defual value
favorite_book('Python Crash Couser')

