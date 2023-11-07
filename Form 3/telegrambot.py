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
TOKEN = "TOKEN"
bot = telebot.TeleBot(TOKEN)  # registers the bot


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if "hi" in message: #use the message.text function
        bot.reply_to(message, "Hello there!")
    else:
        bot.reply_to(message, "I dont understand")


bot.polling() #starts the bot





