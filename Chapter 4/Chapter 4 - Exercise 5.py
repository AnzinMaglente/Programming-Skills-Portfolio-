# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:09:59 2023

@author: Anzin R. Maglente
"""

"""
Chapter 4 - Exercise 5: Favorite Fruit 
Make a list of your favorite fruits, and then write a series of independent if statements that check for certain 
fruits in your list.

•Make a list of your three favorite fruits and call it favorite_fruits.

•Write five if statements. Each should check whether a certain kind of fruit is in your list. 
If the fruit is in your list, the if block

should print a statement,such as You really like bananas!
"""

favorite_fruits = ["apple", "banana", "grapes"] #This is a list of my favorite fruits
print("my favorite fruits are:")
print(favorite_fruits)
print("")
if "apple" in favorite_fruits: #This checks if the element "apple" if in the list "favorite_fruits"
    print ("Wow, you really must love apples\n")
if "watermelon" in favorite_fruits:
    print ("Wow, you really must love watermelons\n")
if "mango" in favorite_fruits:
    print ("Wow, you really must love mangos\n")
if "grapes" in favorite_fruits:
    print ("Wow, you really must love grapes\n")
if "banana" in favorite_fruits:
    print ("Wow, you really must love bananas\n")

"""
This returns three different statements:
    Wow, you really must love apples
    Wow, you really must love bananas
    Wow, you really must love grapes
"""