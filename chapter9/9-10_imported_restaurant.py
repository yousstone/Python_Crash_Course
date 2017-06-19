#! /usr/bin/python3
# -*- coding: utf-8 -*-
'''
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is working
properly.

'''

from restaurant import Restaurant

resa = Restaurant('mo_gu_wu','man_han_quan_xi')
resa.describe_restaurant()
resa.open_restaurant()