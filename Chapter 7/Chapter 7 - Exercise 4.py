# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:31:59 2023

@author: Anzin R. Maglente
"""

"""
Chapter 7 - Exercise 4: Large Shirts
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
"""

def make_shirt (size='large', message='I love Python'): #This creates a default variable for each argument.
    print (f"The size of the t-shirt will be: {size}")
    print (f'and it will have "{message}" written on it.\n')

make_shirt() #This will used the default variable, size = 'large, and message = "I love Python"
make_shirt(size='medium')
make_shirt(size='small', message='The best t-shirt around!') #This changes both arguments to the specified string.