#!/usr/bin/python
# coding=utf8

'''
8-13. User Profile: Start with a copy of user_profile.py from page 153. Build
a profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.
'''

def build_profile(first, last, **user_info):
	''' Bulid a dictionary containing everythin we know about a user.'''
	'''两个星号让python创建一个名为user_info的空字典，并将收到的所有键值对都
	封装到这个字典中'''
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('Michael', 'Jordan',
							city='chicago',
							sprot='basketball')

print (user_profile)