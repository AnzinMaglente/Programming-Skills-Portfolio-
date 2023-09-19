# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:56:18 2023

@author: Anzin R. Maglente
"""

"""
Chapter 3 - Exercise 3: Your Own List
Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples.
Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
"""

Transportation = [
    "Mercedes Benz",
    "Zipline",
    "Old-fashion train",
    "Horse",
    "Sail boat"
    ]

for i in Transportation:
    print("It would be cool to ride a " + i.title() + " someday.")
    print("However, riding a " + i.title() + " would be a hassle due to there being better alternatives in terms of pricing or quality.")
    print("Thus, I would only be riding a " + i.title() + " for the experience\n")
#This does the same thing as the previous programs wherein it prints out a sentence and add each elements in the list