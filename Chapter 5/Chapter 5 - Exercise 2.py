# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 21:55:56 2023

@author: Anzin R. Maglente
"""

"""
Chapter 5 - Exercise 2: Glossary
A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your 
glossary, and store their meanings as values.

Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its
meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character
(\n) to insert a blank line between each word-meaning pair in your output.    
"""

glossary = {
    'string' : 'A sequence of characters that consist of letters, numbers, and symbols.',
    'input' : 'A funtion used to take an input from the user.',
    'reverse' : 'A method to invert the order of a given list.',
    'append' : 'A method to add an element to a given list.',
    'modulus' : 'A arithmetic operator that returns the reminder of a division.',
    }
#This is a dictionary of words I learned and their definitions

print("My Glossary")

word = 'string'
print("\n\t" + word.title() + ": " + glossary[word])
#To get the word you have to write out "___.title" and to get the definition, you write "dictionary_name[___]" 

word = 'input'
print("\n\t" + word.title() + ": " + glossary[word])

word = 'reverse'
print("\n\t" + word.title() + ": " + glossary[word])

word = 'append'
print("\n\t" + word.title() + ": " + glossary[word])

word = 'modulus'
print("\n\t" + word.title() + ": " + glossary[word])