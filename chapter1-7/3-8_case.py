#!/usr/bin/python
# coding=utf8

place = ['qingdao','zhoushan','lijiang','puzhehei','xizhang','jiuzhaigou']
print "---------------origin-----------------"
for i in range(len(place)):
	print place[i]

new_place = sorted(place)
print "-----------------sorted(place)-----------------"
for i in range(len(new_place)):
	print new_place[i]

print "---------------origin-----------------"
for i in range(len(place)):
	print place[i]

new_place_1 = sorted(place,reverse=True)
print "-----------------sorted(place,reverse=True)----------------"
for i in range(len(new_place_1)):
	print new_place_1[i]

print "---------------origin-----------------"
for i in range(len(place)):
	print place[i]


place.reverse()
print "---------------plaece.reverse()----------------"
for i in range(len(place)):
	print place[i]

place.reverse()
print "---------------origin-reverse()*2----------------"
for i in range(len(place)):
	print place[i]

place.sort()
print "---------------plaece.sort()----------------"
for i in range(len(place)):
	print place[i]

place.sort(reverse=True)
print "---------------plaece.sort(reverse=True)----------------"
for i in range(len(place)):
	print place[i]