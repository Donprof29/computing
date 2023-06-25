"""
Author: Don Prof
Date: 23th June, 2023.
Description: The program accepts inputs from the user and
            outputs the largest number. Part 2
Topics: conditional statements, boolean operators
"""

number1 = int(input("Enter a number "))
number2 = int(input("Enter a number "))
number3 = int(input("Enter a number "))
number4 = int(input("Enter a number "))
#check if number1 is larger than the others
if (number1 > number2 and number1 > number3 and number1 > number4):
   print(number1, "is the largest") #output

#check if number2 is larger than the others
elif (number2 > number3 and number2 > number4):
    print(number2, "is the largest")

#check if number3 is larger than the other
elif (number3 > number4):
    print(number3, "is the largest")

else: #this code runs if the condition above is false
   print(number4, "is the largest ") #output