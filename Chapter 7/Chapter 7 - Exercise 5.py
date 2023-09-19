# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:49:46 2023

@author: Anzin R. Maglente
"""

"""
Exercise 5: Cities
Write a function called describe_city() that accepts the name of a city and its country. 
The function should print a simple sentence, such as Reykjavik is in Iceland. Give the 
parameter for the country a default value. Call your function for three different cities, 
at least one of which is not in the default country.
"""

def describe_city(city="Dubai", country="United Arab Emirates"): 
    print (f"{city} is located in {country}")

describe_city()
describe_city(city="Toronto", country="Canada") #This changes both arguments
describe_city(city="Abu Dhabi") #This changes the city argument