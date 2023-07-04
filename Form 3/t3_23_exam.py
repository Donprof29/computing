"""
Author: Team Alpha
Date: 28th June, 2023.
Group Members:


End of Term Examinations.
Problem:
Simo & Sons Pizza sells three types of pizzas: Margherita, Pepperoni, and Vegetarian. The prices of the pizzas are as follows: Margherita - $20, Pepperoni - $30, Vegetarian - $45. Write a program that allows a customer to order a pizza by entering the item number. After placing an order, the customer is asked if they would like to place another order. If the customer answers 'No', the program should end and display a message thanking them for their business. If the customer answers 'Yes', the program should display the menu list again and prompt the customer to enter the item number for their next order."
"""

# start your code after this line
while True: #keeps the whole program in a continuous loop
    menu = ["1. Margherita - $20", "2. Pepperoni - $30", "3. Vegetarian - $45"] #create a menu list
    print("Menu List: ") #output message
    for item in menu: #iterates over each element in the list
        print(item) #output the current element in the list
    item = int(input("Please enter the item number: ")) #accepts user input
    index = item -1 #declares a variable to save the list's index
    if index == 1: #condition
        print(menu[index], "has been ordered") #output
    elif item ==2: #condition
        print(menu[index], "has been ordered")
    elif item == 3: #condition
        print(menu[index], "has been ordered")
    else: #runs when an order is incorrect
        print("Sorry, your order cannot be processed.")
    ans = input("Would you like to order again? ") #accepts user input
    if ans.lower() == "no": #converts text to lowercase and compares with "no"
        print("Thank you for doing business with us")
        break #breaks out of the while loop to end the program
    else:
        print("Great, bringing up menu list") #output
    #if the ELSE block is run, the code in the while loop will start again.

