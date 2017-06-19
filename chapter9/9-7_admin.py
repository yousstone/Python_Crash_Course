#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""
    9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.

"""


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

class Admin(User):
    def __init__(self, first_name, last_name ,age ,gender ,location):
        super().__init__(first_name, last_name, age, gender, location)
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        user_name = self.first_name + ' ' + self.last_name
        print('The lists of %s\'s set of privileges are: '%(user_name))
        for i in self.privileges:
            print(i)

ad = Admin('Michael','Jordan','55','Male','Chicago')
ad.show_privileges()
