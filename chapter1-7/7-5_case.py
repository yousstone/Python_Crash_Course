#!/usr/bin/python
# coding=utf8

# 有家电影院根据观众的年龄收取不同的票价：不到3 岁的观众免费；
# 3~12 岁的观众为10 美元；超过12 岁的观众为15 美元。
# 请编写一个循环，在其中询问用户的年龄，并指出其票价。

prompt = '\nPleas enter your age(between 0 - 100)： '
prompt += '\nIf you want quit ,enter quit '

active = True
while active:
	age = raw_input(prompt)
	if age == 'quit':
		active = False
	else:
		age = int(age)
		if (age < 0 or age > 80):
			print '\nYour age is out of arrange.Sorry'
			continue
		elif age < 3:
			print '\nYou are free to see a movie.'
		elif age <= 12:
			print '\nThe price of your movie ticket is $10.'
		elif age <= 80:
			print '\nThe price of your movie ticket is $15.'

