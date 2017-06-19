#! /usr/bin/python3
# -*- coding: utf-8 -*-
'''
A separate class Admin and Privileges moduel

'''
from users import User

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