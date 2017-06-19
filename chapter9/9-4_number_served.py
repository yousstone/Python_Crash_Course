#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 21:52:16 2017

@author: t450s
"""
'''
9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business.
'''

class Resaurant():

	def __init__(self, name ,cuisine_type):
		self.name = name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_resaurant(self):
		print (self.name,self.cuisine_type)

	def open_resaurant(self):
		print('Welcome ,we %s open!') % self.name
  
resa1 = Resaurant('wang_xiang_yuan','chuan_cai')

print("Reseaurant %s has served %d customers,since it open.") % (resa1.name,resa1.number_served)

resa1.number_served = 100
print("Reseaurant %s has served %d customers,since it open.") % (resa1.name,resa1.number_served)
  

