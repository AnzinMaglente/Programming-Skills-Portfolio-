# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:12:01 2023

@author: Anzin R. Maglente
"""

"""
Chapter 1 - Exercise 3: Print date and Time
Write a Python program to display the current date and time.
"""

import datetime #Same thing as last time but it gets the time from your laptop

now = datetime.datetime.now() #This assigns the current time to a single variable

print ("Current date and time : ")

print (now.strftime("%Y-%m-%d %H:%M:%S")) #This uses year month day - Hour Minute Second to print out the time 