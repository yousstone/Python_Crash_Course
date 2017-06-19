#!/usr/bin/python
# coding=utf8

river = {
	'nile':'Egypt',
	'yangzi':'China',
	'amazon':'USA'
}

for k ,v in river.items():
	print 'The %s runs through %s' % (k,v)