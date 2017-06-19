#! /usr/bin/python3
# -*- coding: utf-8 -*-
'''
9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
'''

class User():
    def __init__(self, first_name, last_name, age, gender, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.location = location

    def describe_user(self):
        user_info = {'first_name': self.first_name,
                     'last_name': self.last_name,
                     'age': self.age,
                     'gender': self.gender,
                     'location': self.location
                     }
        print(user_info)

    def greet_user(self):
        user_name = self.first_name + ' ' + self.last_name
        print
        'Hello %s, have a nice day!' % user_name

class Privileges():

    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        
        print('Privileges are: ')
        for i in self.privileges:
            print(i)

class Admin(User):
    def __init__(self, first_name, last_name ,age ,gender ,location):
        super().__init__(first_name, last_name, age, gender, location)
        self.privileges = Privileges()

ad = Admin('Michael','Jordan','55','Male','Chicago')
ad.privileges.show_privileges()

