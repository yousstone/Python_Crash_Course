#!/usr/bin/python
# coding=utf8

# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.

def describe_city(name,country='China'):
	print('%s is in %s') % (name,country)

describe_city('ShangHai')
describe_city('New York','USA')
describe_city(country='France',name='Paris')