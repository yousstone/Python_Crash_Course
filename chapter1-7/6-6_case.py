#!/usr/bin/python
# coding=utf8

import random

colors=['green','red','blue','black','white','yellow']
points=range(1,11)
speeds=['slow','middle','fast']

aliens=[]

for alien_number in range (0,30):
    new_alien = {
    'color': random.choice(colors), 
    'points': random.choice(points), 
    'speed': random.choice(speeds)
    }
    aliens.append(new_alien)

for i in range (len(aliens)):
	print aliens[i]