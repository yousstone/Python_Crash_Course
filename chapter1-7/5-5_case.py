#!/usr/bin/python
# coding=utf8

import random
# alien_color = random.sample(['green','yellow','red'],1)

for i in range(1,11):
	alien_color1 = random.choice(['green','yellow','red'])

	if alien_color1 == 'green':
		print "You get 5 points!"
	elif alien_color1 == 'yellow':
		print "You got 10 points!"
	elif alien_color1 == 'red':
		print "Your got 15 poins!"
