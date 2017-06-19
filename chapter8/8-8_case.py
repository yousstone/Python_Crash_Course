#!/usr/bin/python3
# coding=utf8

"""8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop."""

def make_album(name,title,count=0):
	if count == 0:
		album_info = {
			'artist':name,
			'title':title
		}
	elif count > 0:
		album_info = {
			'artist':name,
			'title':title,
			'the number of tracks':count
		}
	return album_info

while True:

	first_input = input('Enter "s" to start,enter "q" to quit : ')
	
	if first_input == 'q':
		print 'GAME OVER'
		break
	
	elif first_input == 's':
		name = input('Please enter the artist of new album : ')
		title = input('Please enter the title of new album : ')
		count = input('Please enter the number of the tracks of new album : ')
	
	print ('Your new album is :%s') % make_album(name,title,count)



