#!/usr/bin/python
# coding=utf8

import random

favourite_num = {
	'petter':random.sample(range(1,101),7),
	'michael':random.sample(range(1,101),10),
	'tesla':random.sample(range(1,101),9),
	'kobe':random.sample(range(1,101),12),
	'lily':random.sample(range(1,101),4)
	}

for name ,number in favourite_num.items():
	print '%s\'s favourite number is : ' % name,
	for num in number:
			print num ,
	print