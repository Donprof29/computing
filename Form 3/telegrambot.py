"""
Author: DonProf
Date: 20th October, 2023.
Description: Testing telegram bot using Python language

Step 1: install pyTelegramBotApi using pip install pyTelegramBotApi
Step 2: import telebot
Step 3: Register your telegram token using telebot.TeleBot(TOKEN)
"""

import telebot #imports the telebot library

TOKEN = "REPLACE_YOUR_TOKEN"
bot = telebot.TeleBot(TOKEN) # registers the bot



# all keyboard functions
def start_keyboard():  # function for start keyboard
    start_kb = telebot.types.InlineKeyboardMarkup() #creates an object of the InlineKeyboardMarkup
    start_kb.row(telebot.types.InlineKeyboardButton("Product & Service", callback_data="product"),
    telebot.types.InlineKeyboardButton("Pricing & Packages", callback_data="pricing"))

    start_kb.row(telebot.types.InlineKeyboardButton("Technical Support", callback_data="tech"))

    return start_kb


def product_keyboard(): # Product and Services keyboard
    product_kb = telebot.types.InlineKeyboardMarkup()
    product_kb.row(telebot.types.InlineKeyboardButton("Software solutions", callback_data="software"),
                   telebot.types.InlineKeyboardButton("Cloud Computing", callback_data="cloud"))
    product_kb.row(telebot.types.InlineKeyboardButton("Cybersecurity", callback_data="cyber"))
    return product_kb

def pricing_keyboard(): # Pricing and Packages keyboard
    pricing_kb = telebot.types.InlineKeyboardMarkup()
    pricing_kb.row(telebot.types.InlineKeyboardButton("$0 - $500", callback_data="small"),
                   telebot.types.InlineKeyboardButton("$500 - $1000", callback_data="medium"))
    pricing_kb.row(telebot.types.InlineKeyboardButton("$1000 +", callback_data="large"))
    return pricing_kb

def tech_keyboard(): # Technical Support keyboard
    tech_kb = telebot.types.InlineKeyboardMarkup()
    tech_kb.row(telebot.types.InlineKeyboardButton("Windows", callback_data="windows"),
                   telebot.types.InlineKeyboardButton("Linux", callback_data="linux"))
    tech_kb.row(telebot.types.InlineKeyboardButton("macOS", callback_data="mac"))
    return tech_kb


# the end of keyboard functions



# The function below handles all keyboard selections or callback data
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call): # handles all keyboard responses
    if call.data == "product":
        print("Product selected")
        product_text = "Which area are you interested in?"
        #bot needs the chat.id to contact the user
        bot.send_message(call.message.chat.id, product_text, reply_markup=product_keyboard())
        #calls the product_keyboard function to draw the keyboard

    elif call.data == "pricing":
        print("Pricing selected")
        pricing_text = "What is your budget range?"
        bot.send_message(call.message.chat.id, pricing_text, reply_markup=pricing_keyboard())

    elif call.data == "tech":
        print("Technical selected")
        tech_text = "Which OS are you using?"
        bot.send_message(call.message.chat.id, tech_text, reply_markup=tech_keyboard())

    # end of main menu keyboard responses

    # start of follow-up keyboard responses
    elif call.data == "software":
        print("Software selected")
        software_text = "Good choice software solutions is the best choice for personal use."
        bot.send_message(call.message.chat.id, software_text)

    elif call.data == "cloud":
        print("Cloud selected")
        cloud_text = "Cloud computing is suitable for syncing services and IoT."
        bot.send_message(call.message.chat.id, cloud_text)

    elif call.data == "cyber":
        print("Cybersecurity selected")
        cyber_text = "It's time to hack the hackers."
        bot.send_message(call.message.chat.id, cyber_text)

    # callback for pricing and packages follow-up
    elif call.data == "small":
        print("Basic package selected")
        small_text = "We recommend you purchase the Basic package"
        bot.send_message(call.message.chat.id, small_text)

    elif call.data == "medium":
        print("Premium package selected")
        medium_text = "We recommend you purchase the Premium package"
        bot.send_message(call.message.chat.id, medium_text)

    elif call.data == "large":
        print("Developer package selected")
        large_text = "We recommend you purchase the Developer package"
        bot.send_message(call.message.chat.id, large_text)

    #callback for OS follow-up
    elif call.data == "windows":
        print("Windows selected")
        windows_text = ("Understood. Please try restarting your device and let us know "
                        "if the issue persists. Thank you")
        bot.send_message(call.message.chat.id, windows_text)

    elif call.data == "linux":
        print("Linux selected")
        linux_text = ("Great choice please run sudo apt update or "
                      "sudo dnf update to fix the issue.")
        bot.send_message(call.message.chat.id, linux_text)

    elif call.data == "mac":
        print("macOS selected")
        macOS_text = ("Sorry! you are on your own, we do not support "
                      "mac products because they don't support "
                      "other products also.")
        bot.send_message(call.message.chat.id, macOS_text)

    else:
        print("I cannot understand you.")



#functions for each command
# Start command
@bot.message_handler(commands=['start'])
#function to start message
def start_message(message):
    print("Start command selected")
    message_text = ("Welcome to Bit Cloud, an imaginary IT solutions company, "
                    "aims to enhance its customer service capabilities by developing an "
                    "interactive chatbot. This chatbot is developed to guide clients through their inquiries. "
                    "Please select one of the following.")
    bot.reply_to(message, message_text, reply_markup=start_keyboard()) # for reply to command


# a function to handle the help command
@bot.message_handler(commands=['help'])
def help_command(message):
    print("Help command selected")
    help_text = ("This bot is for an imaginary company called Bit Cloud. NB: The bot was "
                 "designed solely for academic purposes only.")
    bot.reply_to(message, help_text)

#a function to handle the members command
@bot.message_handler(commands=["members"])
def group_members(message):
    print("Member command selected")
    members_text = ("This bot was developed by Team Fedora: \n"
                    "Don Prof \n"
                    "Osei Sark \n"
                    "Elinam \n"
                    "Kofi Asante \n"
                    "Macario \n"
                    "Ron \n"
                    "Jose"
                    )
    bot.reply_to(message,members_text)



# function to handle bot chatting. Natural Language Processing
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower() # converts the text to lowercase for case-insensitive matching
    if "hi" in text:
        bot.reply_to(message, "Hello there!")
    elif "bye" in text:
        bot.reply_to(message, "The bye is good")
    elif "good morning" in text:
        bot.reply_to(message, "The morning is good")
    elif "good afternoon" in text:
        bot.reply_to(message, "The afternoon is good")
    elif "good evening" in text:
        bot.reply_to(message, "The evening is good")
    else:
        bot.reply_to(message, "I'm sorry, I don't understand. Could you please rephrase?")

    #this prints out the message sent and the user
    print_user_info(message.from_user, message.text)


#function to print out the data of user in the console
def print_user_info(user, message_text):
    if user.username:
        print(f"Username: @{user.username} sent -> {message_text}")
    elif user.first_name:
        print(f"First Name: {user.first_name} sent -> {message_text}")


# start bot by polling method
print("Bot is starting... ")
print("Polling...")
bot.polling()
