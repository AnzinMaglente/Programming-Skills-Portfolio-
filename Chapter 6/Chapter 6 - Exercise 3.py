# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 16:32:11 2023

@author: Anzin R. Maglente
"""

"""
Chapter 6 - Exercise 3: Infinity
Write a loop that never ends, and run it. (To end the loop, press ctrl-C or close the window displaying the output.)
"""

prompt = """\nCrazy? I was crazy once. They locked me in a room, a rubber room,
a rubber room with rats and rats make me crazy. """
prompt += "\n\npress anything to continue: "

while True:
    Crazy = input(prompt)

"""
This is a loop that does not end, the only way to end is ctrl-C or closing the window of the output.
It will ask the user if they want to continue it, but has no way to end naturally
"""