#! /usr/bin/python3
# -*- coding: utf-8 -*-
'''
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178).
Store the classes User, Privileges, and Admin in one module. Create a separate
file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.
'''

from user import User
from user import Privileges
from user import Admin

ad = Admin('Michael','Jordan','55','Male','Chicago')
ad.privileges.show_privileges()
ad.describe_user()
ad.greet_user()