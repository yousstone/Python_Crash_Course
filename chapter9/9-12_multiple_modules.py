#! /usr/bin/python3
# -*- coding: utf-8 -*-
'''
9-12. Multiple Modules: Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.
'''
from admin_privileges import Admin
ad = Admin('Michael','Jordan','55','Male','Chicago')
ad.privileges.show_privileges()