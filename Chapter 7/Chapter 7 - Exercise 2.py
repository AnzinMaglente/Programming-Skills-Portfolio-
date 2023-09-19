# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:23:37 2023

@author: Anzin R. Maglente
"""

"""
Chapter 7 - Exercise 2: Favorite Book 
Write a function called favorite_book() that accepts one parameter, title. The function should print a message, 
such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title 
as an argument in the function call.
"""

def favorite_book(book, author): #This uses several elements that can be changed when using the definition
    print (f"My favorite book is '{book}' by: {author}.")

favorite_book("The Empty Box of Zeroth Maria", "Eiji Mikage")
"""
The "Empty Box of Zeroth Maria", will change the book argument
While "Eiji Mikage" will change the author argument
"""