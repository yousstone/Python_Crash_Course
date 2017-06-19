#!/usr/bin/python3
# coding=utf8

'''8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding
the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified.'''

def make_great(names):
	for i in range(len(names)):
		names[i] = 'The Great ' + names[i]
	return names
		
def show_magicians(names):

	print ('The names of each magicians: ')
	for name in names:
		print name



magician_names = ['Ada','Berg','Kaley']
great_magician = make_great(magician_names)
show_magicians(magician_names)