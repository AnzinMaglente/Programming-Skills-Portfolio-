# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 12:52:55 2023

@author: Anzin R. Maglente
"""

"""
Chapter 3 - Exercise 1: Names
Store the names of a few of your friends in a list called names. Print each person’s name by
accessing each element in the list, one at a time
"""

my_friends = ["Cid", "James", "Ericka", "Lianne", "Carl"] #This is a list to store multiple variables
print ("These are my friends:")
for i in my_friends:
    print ("\t", i.title())

"""
This is just a quick way to list down the names one by one 
without having to make multiple lines stating:
    print (my_friends[0])
    print (my_friends[1])
    and so on
It uses the 'for' function to print out each element inside the list
"""
