# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 22:29:59 2017

@author: t450s
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.

"""

class Resaurant():
	def __init__(self, name ,cuisine_type):
		self.name = name
		self.cuisine_type = cuisine_type

	def describe_resaurant(self):
		print(self.name,self.cuisine_type)

	def open_resaurant(self):
		print('Welcome ,we %s open!') % self.name

class IceCreamStand(Resaurant):
	def __init__(self, name ,cuisine_type):
		super().__init__( name, cuisine_type)
		self.flavors = ['Bacon','Beer','English toffee']

	def display_flavors(self):
		print('The ice cream\'s flavors includes following: ')
		for f in self.flavors:
			print(f)

ic = IceCreamStand('Honey','Vanilla')

ic.display_flavors()
