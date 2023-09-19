# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:21:04 2023

@author: Anzin R. Maglente
"""

"""
Exercise 3: Alien Colors #3
Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

• If the alien is green, print a message that the player earned 5 points.

• If the alien is yellow, print a message that the player earned 10 points.

• If the alien is red, print a message that the player earned 15 points.

• Write three versions of this program, making sure each message is printed for the appropriate color alien.
"""

alien_color = "red"

if alien_color == "green": #This checks if the alien is color green if true it will print out the following message
    print("You earned 5 points")
elif alien_color == "yellow": #If not it check's if the alien is yellow
    print("You earned 10 points")
elif alien_color == "red": #Tastly, if it isn't yellow or red. It checks if it is red
    print("You earned 15 points")
    
#The third if statement is true, therefore it returns as "you earned 15 points"