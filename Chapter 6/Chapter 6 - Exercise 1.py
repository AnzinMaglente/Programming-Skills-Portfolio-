# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:57:06 2023

@author: Anzin R. Maglente
"""

"""
Chapter 6 - Exercise 1: Pizza Toppings
Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
As they enter each topping, print a message saying you’ll add that topping to their pizza.
"""

print ("""Hello, welcome to Pizza Time! What would you want on your pizza?
If you want to exit out of this program please write 'quit'""")

while True: #This is a while function that returns to the start whenever the statement is true
    topping = input("\nWhat toppings would you like for your pizza?\n\t")
    if topping != 'quit': #if the user writes out "quit", it will end the program, if not. It loops back in itself.
        print ("\nI'll add " + topping + " on to your pizza!")
    else:
        break #Break is used to end a loop