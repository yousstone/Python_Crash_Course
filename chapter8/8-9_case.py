#!/usr/bin/python3
# coding=utf8
'''
8-9. Magicians: Make a list of magician’s names.
 Pass the list to a functioncalled show_magicians(), 
 which prints the name of each magician in the list.
'''

def show_magicians(names):
	print ('The names of each magicians: ')
	for name in names:
		print name

magician_names = ['Ada','Berg','Kaley']
show_magicians(magician_names)

