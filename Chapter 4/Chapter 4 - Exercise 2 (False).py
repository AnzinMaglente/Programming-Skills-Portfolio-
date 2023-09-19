# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:21:04 2023

@author: Anzin R. Maglente
"""

"""
Chapter 4 - Exercise 2: Alien Colors #2
Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

•If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.

•If the alien’s color isn’t green, print a statement that the player just earned 10 points.

•Write one version of this program that runs the if block and another that runs the else block.
"""

alien_color = "yellow"

if alien_color == "green": #This checks if the alien is color green if true it will print out the following message
    print("You earned 5 points")
else: #If it is false, the program will print this message
    print("You earned 10 points")
#The condition is false, it returns "You earned 10 points"