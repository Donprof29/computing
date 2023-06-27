"""
Author: Don Prof
Date: 26th June, 2023.
Description: Replace an item in a list
Topic: list, conditional statement
"""
studentNames  = ["Simo",
                 "Red Fox",
                 "Joe",
                 "Sikani",
                 "Mawuena"] #creates a list
print("Your username is", studentNames[3])
ans = input("Do you want to change it? ") #accepts user input

if ans == "Yes" or "yes": #checks if user input is yes or Yes
    newName = input("Enter your new name") #accepts user input
    studentNames[3] = newName #replace item in index 3
    print("Your username is now",
      studentNames[3]) #output item in index 3
else:
    print("Username saved")

