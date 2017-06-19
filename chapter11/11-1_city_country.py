#!/usr/bin/python3
# coding=utf8
'''
11-1. City, Country: Write a function that accepts two parameters: a city name
and a country name. The function should return a single string of the form
City, Country, such as Santiago, Chile. Store the function in a module called
city_functions.py.
Create a file called test_cities.py that tests the function you just wrote
(remember that you need to import unittest and the function you want to test).
Write a method called test_city_country() to verify that calling your function
with values such as 'santiago' and 'chile' results in the correct string. Run
test_cities.py, and make sure test_city_country() passes.
'''

from city_function import get_city_country

print ("Enter 'q' at any time to quit.")
while True:
    city = input("\nPlease enter your city: ")
    if city == 'q':
        break
    country = input("\nPlease enter your country: ")
    if country == 'q':
        break

    full_name = get_city_country(city,country)
    print("\tNeatly name: " + full_name + ".")
