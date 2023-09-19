# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:21:06 2023

@author: Anzin R. Maglente
"""


"""
Chapter 2 - Exercise 5: USB Shopper
A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. 
They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise.
"""

print ("""
A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. 
They are £6 each. 

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
""")

Money = 50
USB = 6
Final_Amount = str(int(Money/USB))
Reminder = str(int(Money%USB))

#Again using arithmetic functions, you are able to divide the money with the cost of USB sticks and get your reminder

print ("Our variables are:\n\tGirl's money = £50\n\tCost of USB sticks = £6\nTherefore, you would need to divide 50 with 6 to get the total USB sticks she can buy\n\t the total would be " + Final_Amount + " USBs with a reminder of £" + Reminder)

