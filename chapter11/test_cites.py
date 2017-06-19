#!/usr/bin/python3
# coding=utf8
import unittest
from city_function import get_city_country

class CityTestCase(unittest.TestCase):
    """Tests for 'city_function.py'."""

    def test_city_country(self):
        """Do city country like 'shanghai' 'China' work？"""
        city_country = get_city_country('shanghai', 'China')
        self.assertEqual(city_country,'shanghai, China' )

    def test_city_country_population(self):
        """Do city country population like 'shanghai' 'China' 20000000 work? """
        city_country_population = get_city_country('shanghai', 'China', 20000000)
        self.assertEqual(city_country_population, 'shanghai, China 20000000')


unittest.main()