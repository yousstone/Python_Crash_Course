#!/usr/bin/python
# coding=utf8

for i in range(3,31,3):
	print i
print '--------'
for i in [x for x in range(3,31) if x % 3 == 0 ]:
	print i