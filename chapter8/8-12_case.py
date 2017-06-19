#!/usr/bin/python
# coding=utf8

'''
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that is being ordered. Call the function three times, using a different number
of arguments each time.

'''

def make_sandwich(*toppings):
	# *让python创建一个名为toppings的空元组(tuple),将所有调用时使用的参数
	# 都封装到这个元组中，哪怕只有个参数，也是放入元组中，所以无论多少个参数，
	# 实现方式都是如此
	print ('Making a sandwich with the following toppings: ')
	for topping in toppings:
		print ('-' + topping)

make_sandwich('spinach','carrots','sprouts')
make_sandwich('pickles')
make_sandwich('olives','mushrooms')