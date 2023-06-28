"""
Author: Don Prof
Date: 27th June, 2023.
Description: Using list functions
Topic: list, functions
"""
playerNames = ["Messi", "Ronaldinho", "Neymar", "Ronaldo", "Suarez"] #creates a list
print(playerNames) #outputs items in the list
playerNames.append("Haaland") #adds an item to the list
print(playerNames) #outputs items in the list
playerNames.insert(2, "Rashford") #adds an item to index 2
print(playerNames) #outputs items in the list
coachNames = ["Phestus", "Erik", "Zidane", "Ferguson" ] #creates a list
playerNames.extend(coachNames) #joins coachNames list to playerNames list
print(playerNames) #outputs items in the list
playerNames.remove("Phestus") #removes an item in the list
print(playerNames) #outputs items in the list