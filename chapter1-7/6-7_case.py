#!/usr/bin/python
# coding=utf8

acquaintance = {
	'first_name':'Michael',
	'last_name':'Jordan',
	'age':55,
	'city':'chicag'
	}


friends = {
	'first_name':'Michael1',
	'last_name':'Jordan1',
	'age':56,
	'city':'shanghai'
}

classmates = {
	'first_name':'Michael2',
	'last_name':'Jordan2',
	'age':57,
	'city':'beijing'
}

peoples = [acquaintance,friends,classmates]

for people in peoples:
	for key ,value in sorted(people.items())  :
		print key , value
		print r