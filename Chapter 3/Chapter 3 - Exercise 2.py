# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 12:52:55 2023

@author: Anzin R. Maglente
"""

"""
Chapter 3 - Exercise 2: Greetings
Start with the list you used in Exercise 1, but instead of just printing each person’s name, 
print a message to them. The text of each message should be the same, but each message should 
be personalized with the person’s name.

"""

my_friends = ["Cid", "James", "Ericka", "Lianne", "Carl"]
message = ("Hello, how are you today ") #This is the message I want to send to my friends

for i in my_friends:
    print(message + i.title() + "?")
#Same as last time, but now with it prints a sentence alongside my friends