# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 16:41:54 2023

@author: Anzin R. Maglente
"""

"""
Chapter 6 - Exercise 4: Deli
Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called 
finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your 
tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been 
made, print a message listing each sandwich that was made.
"""

sandwich_orders = ["Pastrami", "Club", "Tuna", "Turkey", "Grilled cheese"] #This list is orders from the customer
finished_sandwiches = [] #This empty list will be used when the sandwiches are ready

print ("""Hello! Welcome to Subway what would you like?

...

Okay, right away!\n""")

while sandwich_orders:
    cooking_sandwich = sandwich_orders.pop() #This removes the first element in the list "sandwich_order"
    print(f"your {cooking_sandwich} sandwich is currently being prepared, please wait for a moment.")
    finished_sandwiches.append(cooking_sandwich) #And this adds the removed element into the list "finished_sandwiches"

print ("\nALright it is done, here is your order!\n")
for sandwich in finished_sandwiches:
    print(f"\tI made an {sandwich} sandwich for you") #This prints out all of the finished sandwiche