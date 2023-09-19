# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:29:27 2023

@author: Anzin R. Maglente
"""

"""
Chapter 3 - Exercise 6: Shrinking Guest List
You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only 
two guests.

•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only 
two people for dinner.

•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop 
a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

•Print a message to each of the two people still on your list, letting them know they’re still invited.

•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you 
ctually have an empty list at the end of your program.  
"""

Invitees = ["Lianne", "Carl", "Elex", "Kent", "Aki"]
for i in Invitees:
    print ("Dear " + i.title() + """.
           You have been cordinally invited to my house for dinner, 
           please respond as soon as possible, thank you\n""")

print("However, " + Invitees[0] + " is unable to come, so a new list was made\n")
Invitees.pop(0) #The pop function works similarly with the .delete function
Invitees.append("Fadi")
for i in Invitees:
    print ("Dear " + i.title() + """,
           You have been cordinally invited to my house for dinner, 
           please respond as soon as possible, thank you\n""")
           
print("""That was until I realized that I could have only invited two people
      (cause the house ain't that big), and so I had to send out a message to the following:""")
Sorry = []
Sorry.append(Invitees[0]) #This adds the first invitee to the list "Sorry"
Invitees.pop(0) #This then deletes the first invitee in the list "Invitee"
Sorry.append(Invitees[2])
Invitees.pop(2)
Sorry.append(Invitees[1])
Invitees.pop(1)

for i in Sorry:
    print("Dear " + i.title() + """,
          I sadly have to inform you that you are no longer invited to dinner,
          due to some unforeseen circumstances, I hope you understand.
          """)

print("And all that remained was two, " + Invitees[0] + " and " + Invitees[1] + "\n")

for i in Invitees:
    print("Dear " + i.title() + """,
          You are still invited to dinner, please don't forget. This is just a
          reminder, thank you in advance.
          """)

del Invitees #I tried printing Invitees after this, it showed up as an error