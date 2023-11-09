'''
Author: Team Fedora
Group Members:
            Kofi Asante
            Nana Osei
            Abbey
Date: 2nd November, 2023.
Description: A bot to help you purchase a game

Step 1: Use the terminal to run "pip install pyTelegramBotAPI"

'''

import telebot  #imports the telebot library
TOKEN = "REPLACE_YOUR_TOKEN"
bot = telebot.TeleBot(TOKEN)  # registers the bot


@bot.message_handler(func=lambda message: True)
def handle_message(message): # parameter
    text = message.text.lower() #changes the message text to lower case
    #selection statement
    if "hi" in text: #use the message.text function

        bot.reply_to(message, "Hello there!") #argument
    elif "good morning" in text:
        bot.reply_to(message, "Morning good")
    elif "how you" in text:
        bot.reply_to(message, "I am doing very great.")
    else:
        bot.reply_to(message, "I dont understand")

    # call the print_user_info function
    print_user_info(message.from_user, message.text)

#create a function to print out the message 
# text sent by a user to the bot

def print_user_info(user, message_text):
    if user.username: # checks if the person has a username
        print(f"Username: @{user.username} sent: {message_text}")
    elif user.first_name: # uses the person's first name
        print(f"First Name: {user.first_name} sent: {message_text}")




print("Bot is starting... ")
bot.polling() #starts the bot





