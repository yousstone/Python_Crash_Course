#!/usr/bin/python
# coding=utf8

user_names = ['mimo','admin','doctor','patient','family']

for name in user_names:
	if name == 'admin':
		print "Hello %s ,would you like to see a status report?" % name
	else:
		print "Hello %s ,welcome to logging again." % name


