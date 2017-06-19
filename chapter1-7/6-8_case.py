#!/usr/bin/python
# coding=utf8

kitty = {
	'type':'cat',
	'owner':'Tesla'
}

mongo = {
	'type':'tiger',
	'owner':'Michael'	
}

feily = {
	'type':'bird',
	'owner':'Lily'
}

pets = [kitty,mongo,feily]


for pet in pets:
	for ty ,ow in pet.items():
		print ty ,ow 
	print