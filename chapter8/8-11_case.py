#!/usr/bin/python
# coding=utf8

'''
8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original
names and one list with the Great added to each magician’s name.
'''
def make_great(names):
	for i in range(len(names)):
		names[i] = 'The Great ' + names[i]
	return names
		
def show_magicians(names):

	print ('The names of each magicians: \n')
	for name in names:
		print name
	print '\n'


magician_names = ['Ada','Berg','Kaley']
magician_names_copy = magician_names[:]

great_magician_copy = make_great(magician_names_copy)

show_magicians(magician_names)
show_magicians(great_magician_copy)