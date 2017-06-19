#!/usr/bin/python
# coding=utf8

a = []
for j in range(10):
	for i in range(1000):
		a.append(i)


for i in a:
	if i == 2:
		a.remove(2)

print len(a)
print 'end'
