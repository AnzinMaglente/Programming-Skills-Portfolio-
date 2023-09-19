# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 09:45:51 2023

@author: Anzin R. Maglente
"""

"""
Chapter 5 - Exercise 4: Rivers
Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 
'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

Use a loop to print the name of each river included in the dictionary.

Use a loop to print the name of each country included in the dictionary.
"""

rivers = {
    'Cagayan River' : 'Philippines',
    'Godavari River' : 'India',
    'Loire River' : 'France',
    'Rochor River' : 'Singapore',
    'Murray River' : 'Australia',
    }
#This stores the rivers and where they run through

print ("Rivers and where they run through")

for river, country in rivers.items():
    print (f"\tThe {river.title()} flows through {country.title()}.")
#This gives out the basic sentence with all the information

print ("\nThe following rivers are included in the 'Rivers and where they run through' section:")
for river in rivers.keys():
    print (f"\t- {river.title()}")
#This only prints out the list of rivers in the "rivers" dictionary
    
print ("\nThe following countries are included in the 'Rivers and where they run through' section:")
for country in rivers.values():
    print (f"\t- {country.title()}")
#This only prints out the list of countries in the "rivers" dictionary