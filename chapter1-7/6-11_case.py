#!/usr/bin/python
# coding=utf8

citys = {
	'Shanghai':{
		'country':'China',
		'population':'25000000',
		'fact':'The most biggest city of China'
	},
	'Tokyo':{
		'country':'Japan',
		'population':'20000000',
		'fact':'The most biggest city of Japan'
	},
	'NewYork':{
		'country':'USA',
		'population':'15000000',
		'fact':'The most biggest city of USA'
	}
}

for city, cpf in citys.items():
	print city
	for key , value in cpf.items():
		print key ,':',value
	print