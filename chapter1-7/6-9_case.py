#!/usr/bin/python
# coding=utf8

favorite_places = {
	'Jay':['TaiBei','HuaLian','JiLong'],
	'wanglihong':['California','Beijing'],
	'gaoxiaosong':['Paris','London','ShangHai']
}

for name ,place in favorite_places.items():
	print '%s\'s favorite places are:' % name ,
	for pla in place:
		print pla, 
	print