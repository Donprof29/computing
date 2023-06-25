"""
Author: Don Prof
Date: 23th June, 2023.
Description: The program accepts inputs from the user and
            performs arithmetic operators on them.
Topics: arithmetic operators, conditional statements
"""

num1 = int(input("Enter a number ")) #accepts user input
num2 = int(input("Enter a number ")) #accepts user input
operator = input("Enter an operator ") #accepts user input
if operator == "+": #return true if operator is +
    sum = num1 + num2
    print("The sum is:", sum) #output
    
elif operator == "-": #return true if operator is -
    difference = num1 - num2
    print("The difference is:", difference) #output

elif operator == "*": #returns tre if operator is *
    product = num1 * num2
    print("The product is:", product)

else: #executes if the above condition prove false
    quotient = num1 / num2
    print("The quotient is:", quotient)