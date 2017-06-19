#! /usr/bin/python3
# -*- coding: utf-8 -*-
'''
A separate class moduel

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
        print('Hello %s, have a nice day!' % user_name)

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




