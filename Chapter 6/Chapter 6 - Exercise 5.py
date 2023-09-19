# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:07:27 2023

@author: Anzin R. Maglente
"""

"""
Chapter 6 - Exercise 5: No Pastrami
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code

near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all

occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
"""

sandwich_orders = ["Pastrami", "Club", "Tuna", "Turkey", "Pastrami", "Roast Beef", "Grilled Cheese", "Pastrami"]
finished_sandwiches = []

print ("""Hello! Welcome to Subway what would you like?

...

Oh sorry, we ran out of pastrami, but we are able to fulfill your other orders\n""")

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
"""This removes any "Pastrami" element from the sandwich_orders list so it would not appear inside the 
finished_sandwiches list.
"""

while sandwich_orders:
    cooking_sandwich = sandwich_orders.pop()
    print(f"your {cooking_sandwich} sandwich is currently being prepared, please wait for a moment.")
    finished_sandwiches.append(cooking_sandwich)

print ("\nALright it is done, here is your order!\n")
for sandwich in finished_sandwiches:
    print(f"\tI made an {sandwich} sandwich for you")