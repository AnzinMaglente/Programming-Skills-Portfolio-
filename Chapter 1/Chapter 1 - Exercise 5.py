# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:15:35 2023

@author: Anzin R. Maglente
"""

"""
Chapter 1 - Exercise 5: Compute area of Circle
Write a Python program which accepts the radius of a circle from the user and compute the area.
"""

from math import pi #This gets from the math database and imports a specific file called "pi"
r = float(input("input the radius of the circle : "))
print ("The area of the circle with the radius of " + str(r) + " is : " + str(pi*r*2))
#This uses arithmetic operators (+, -, *, /, %) to compute the area of a circle