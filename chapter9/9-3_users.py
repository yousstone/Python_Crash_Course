#!/usr/bin/python
# coding=utf8
'''
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
'''

class User():
	def __init__(self ,first_name, last_name ,age ,gender ,location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.gender = gender
		self.location = location		

	def describe_user(self):
		
		user_info = {'first_name':self.first_name,
					 'last_name':self.last_name,
					 'age':self.age,
					 'gender':self.gender,
					 'location':self.location
		}
		print(user_info)

	def greet_user(self):
		user_name = self.first_name + ' ' + self.last_name
		print 'Hello %s, have a nice day!' % user_name

MJ = User('Micheal','Jordan',55,'Male','Chicago')

MJ.describe_user()
MJ.greet_user()

