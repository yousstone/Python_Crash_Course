#!/usr/bin/python
# coding=utf8
'''
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
'''


class Restaurant():
	def __init__(self, name ,cuisine_type):
		self.name = name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print (self.name,self.cuisine_type)

	def open_restaurant(self):
		print('Welcome ,we %s open!') % self.name


resa1 = Restaurant('chihuoqun','shu')

resa1.describe_restaurant()
resa1.open_restaurant()

resa2 = Restaurant('wang_xiang_yuan','chuan_cai')
resa2.describe_restaurant()
resa2.open_restaurant()



