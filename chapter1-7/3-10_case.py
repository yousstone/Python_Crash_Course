#!/usr/bin/python
# coding=utf8

city = ['beijing','shanghai','guangzhou','hefei','hanghzou']

print city
print city.pop()
print city
city.insert(0,'shenzhen')
print city
del city[4]
print city
city.remove('guangzhou')
print city
city.append('nanjing')
print city

city.sort()
print city
city.sort(reverse=True)
print city
