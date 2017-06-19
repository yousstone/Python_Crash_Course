#!/usr/bin/python
# coding=utf8

user_names = ['mimo','admin','doctor','patient','family']

for i in range(len(user_names)):
	# del user_names[0]
	user_names.pop()

if not user_names: # user_name为空返回False，not user_name就是True
		# 只有在user_names 为空时才执行
		print 'we need some users'

for name in user_names:
	if name == '':
		print 'we need some users'
	if name == 'admin':
		print "Hello %s ,would you like to see a status report?" % name
	else:
		print "Hello %s ,welcome to logging again." % name



