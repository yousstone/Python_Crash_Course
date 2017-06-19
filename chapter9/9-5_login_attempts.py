# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 22:18:34 2017

@author: t450s
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.

"""

class User():
	def __init__(self ,first_name, last_name ,age ,gender ,location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.gender = gender
		self.location = location
		self.login_attempts = 0	

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

	def increment_login_attempts(self):
		self.login_attempts = self.login_attempts + 1
  
  	def reset_login_attempts(self):
  		self.login_attempts = 0

MJ = User('Micheal','Jordan',55,'Male','Chicago')

print(MJ.login_attempts)
print ('-'*40)

for i in range(10):
	MJ.increment_login_attempts()
	print(MJ.login_attempts)

MJ.reset_login_attempts()
print ('-'*40)
print(MJ.login_attempts)

