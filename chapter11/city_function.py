#!/usr/bin/python3
# coding=utf8
def get_city_country(city,country,population=0):
    if population:
        city_country_population = city + ", " + country
    else:
        city_country_population = city + ", " + country + ' ' + str(population)
    return city_country_population

