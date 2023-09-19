# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:13:54 2023

@author: Anzin R. Maglente
"""

"""
Chapter 5 - Exercise 5: Pets
Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the 
kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your 
list and as you do, print everything you know about each pet
"""

pets = [] #This empty list will be the place where we store all of the information about each pet

pet = {
       'Name' : 'Pusa',
       'Owner' : 'Anzin',
       'Kind of animal' : 'British Shorthair Persian Cat',
       'Age' : '11 years old',
       'Gender' : 'Male'}

pets.append(pet)
"""
This is an example of one pet, and how it is placed in the 'pets' list
"""

pet = {
       'Name' : 'Mitski',
       'Owner' : 'Andrea',
       'Kind of animal' : 'Corgi Dog',
       'Age' : '1 year old',
       'Gender' : 'Female'}
pets.append(pet)

pet = {
       'Name' : 'Smokey',
       'Owner' : 'Fadi',
       'Kind of animal' : 'American Shorthair Persian Cat',
       'Age' : '4 years old',
       'Gender' : 'Male'}
pets.append(pet)

for pet in pets:
    print(f"\n{pet['Name'].title()} Data:")
    for key, value in pet.items():
        print(f"\t{key} : {value}")
#This prints out the data of each pet inside the list