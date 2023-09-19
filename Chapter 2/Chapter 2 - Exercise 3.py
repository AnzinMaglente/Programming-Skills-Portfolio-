# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:38:52 2023

@author: Anzin R. Maglente
"""

"""
Chapter 2 - Exercise 3: Stripping Names
Tidy up the code to make it easier to understand

Use a variable to represent a person’s name, and include some whitespace characters at the beginning 
and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

Print the name once, so the whitespace around the name is displayed.

Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
"""

Name = " Anzin Maglente "
Name_remove_leading = Name.lstrip() #This removes the spacings from the start of the name
Name_remove_trailing = Name.rstrip() #This removes the spacings from the end of the name
Name_remove_both = Name.strip() #This removes the spacings from the both sides of the name
print ("My name:\n\t_" + Name + "_\nMy name without the leading white space:\n\t" + "_" + Name_remove_leading + "_\nMy name without the trailing white space\n\t" + Name_remove_trailing + "_\nMy name without both white spaces\n\t_" + Name_remove_both + "_")
#I added some underscores to make it more the blank spaces more visible