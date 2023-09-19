# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:31:59 2023

@author: Anzin R. Maglente
"""

"""
Chapter 7 - Exercise 3: T-Shirt
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function 
once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
"""

def make_shirt (size, message):
    print (f"The size of the t-shirt will be: {size}")
    print (f'and it will have "{message}" written on it.\n')

make_shirt('medium', 'Hello world')
make_shirt(message="Hey! Python", size='large') 
#This is a positional argument where you write out the message and size with their equivalent string. 