#!/usr/bin/python
# coding=utf8

# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album. If the calling line includes a value for the number
# of tracks, add that value to the album’s dictionary. Make at least one new
# function call that includes the number of tracks on an album.

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

album1 = make_album('Adale','Today')
album2 = make_album('Bob','Yesterday once more')
album3 = make_album('Califiy','Tomorrow is another day')

print (album1)
print (album2)
print (album3)

album4 = make_album('David','What\'s new',10)
print (album4)