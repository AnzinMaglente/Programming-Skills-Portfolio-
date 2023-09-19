# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:50:20 2023

@author: Anzin R. Maglente
"""

"""
Chapter 4 - Exercise 4: Stages of Life
Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:

•If the person is less than 2 years old, print a message that the person is a baby.

•If the person is at least 2 years old but less than 4, print a message that the person is a toddler.

•If the person is at least 4 years old but less than 13, print a message that the person is a kid.

•If the person is at least 13 years old but less than 20, print a message that the person is a teenager.

•If the person is at least 20 years old but less than 65, print a message that the person is an adult.

•If the person is age 65 or older, print a message that the person is an elder.
"""

age = 17 #This is an example, feel free to change this number

if age > 0 and age < 2: #This checks if the person is greater than 0 years old and if they are less than 2 years old
    print("you are a baby!")
elif age >= 2 and age < 4:
    print("You are a toddler!")
elif age >= 4 and age < 13:
    print("You are a kid!")
elif age >= 13 and age < 20:
    print("You are a teenager!")
elif age >= 20 and age < 65:
    print("You are a adult!")
elif age >= 65:
    print("You are a elder!")

#For this particular instance, the age is between 13 and 20. Therefore, it returns that "You are a teenager"