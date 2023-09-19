# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 16:20:24 2023

@author: Anzin R. Maglente
"""

"""
Chapter 6 - Exercise 2: Movie Tickets
A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, 
the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
Write a loop in which you ask users their age, and then tell them the cost of their movie ticket
"""

movie_prompt = "\nHow old are you?"
movie_prompt += "\nEnter 'quit' if you are finished.\n\t" #This adds a statement from the intial sentence

while True:
    age =  input(movie_prompt)
    if age == 'quit': #Tf the user writes out "quit", it will end the program, if not. It loops back in itself
        break
    age = int(age) #This chances the input into a interger so it can be read in the if statements
    if age < 3: #Checks if you are below 3 years old
        print ("\nFor you the ticket is free.")
    elif age < 13: #Checks if you are below 13 years old
        print ("\nThat will be $10.")
    else:  #Else is used if all the if statements return as false
        print ("\nThat will be $15.")