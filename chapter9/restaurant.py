#!/usr/bin/python
# coding=utf8
'''
A separate class Restaurant

'''


class Restaurant():
	def __init__(self, name ,cuisine_type):
		self.name = name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print (self.name,self.cuisine_type)

	def open_restaurant(self):
		print('Welcome ,we %s open!' % self.name)