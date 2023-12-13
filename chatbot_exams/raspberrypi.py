'''
Author: Team Raspberrypi
Group Members:
              Manasseh
              Nana Yaw
              Manel
              Olivia
Date:22nd November, 2023
Description: A bot to help you purchase a game

step 1: Use the terminal to run "pip install pyTelegramBotAPI"


'''

import telebot  # imports the telegram library

TOKEN = "YOUR_TOKEN"
bot = telebot.TeleBot(TOKEN)  # registers the bot

#functions for all keyboard
def start_keyboard():
    #create an object for the keyboardmarkup()
    start_kb =telebot.types.InlineKeyboardMarkup()
    start_kb.row(telebot.types.InlineKeyboardButton("Blox fruits", callback_data="Pirate or marine"))

    start_kb.row(telebot.types.InlineKeyboardButton("play trial",callback_data="play"))
    return start_kb


def login_keyboard():
    # create an object for the keyboardmarkup()
    login_kb = telebot.types.InlineKeyboardMarkup()
    login_kb.row(telebot.types.InlineKeyboardButton("login", callback_data="log"))

    login_kb.row(telebot.types.InlineKeyboardButton("signup", callback_data="sign"))
    return login_kb


def social_keyboard():
    # create an object for the keyboardmarkup()
    social_kb = telebot.types.InlineKeyboardMarkup()
    social_kb.row(telebot.types.InlineKeyboardButton("sign with google", callback_data="google"))

    social_kb.row(telebot.types.InlineKeyboardButton("sign with facebook", callback_data="facebook"))
    return social_kb



def social_keyboard():
    # create an object for the keyboardmarkup()
    social_kb = telebot.types.InlineKeyboardMarkup()
    social_kb.row(telebot.types.InlineKeyboardButton("multiplayer", callback_data="zombie mode"))

    social_kb.row(telebot.types.InlineKeyboardButton("", callback_data="facebook"))
    return social_kb
# end of all keyboard function




#function for callback
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == "blox":
        print("Blox Fruit selected")
        blox_text = "Which area are you interested in?" #change message
        bot.send_message(call.message.chat.id, "text", reply_markup=blox_keyboard())
    elif call.data == "play":
        print("Play Trial selected")
        play_text = "Which area are you interested in?" #change message
        bot.send_message(call.message.chat.id, "text", reply_markup=play_keyboard())
    elif call.data == "log":
        print("Login selected")
    play_text = "Which area are you intrested in?"  # change message
    bot.send_message(call.message.chat.id, "text", reply_markup=log())

#end of function for callback



#function for start command

@bot.message_handler(commands=["start"])
def start_messege(message):
    print("start command selected")
    message_text = "welcome to Manzium Games,a gaming bot that helps you through your gaming experience."
    bot.reply_to(message, message_text, reply_markup=start_keyboard())



@bot.message_handler(commands=["members"])
def group_members(message):
    print("Members command selected")
    members_text =("This bot was developed by Manzium1_bot Int: \n" 
                   "Nana Yaw \n"
                   " Manasseh \n" 
                   "Olivia \n"
                   "Manel \n"
                   "Macario \n")
    bot.reply_to(message, members_text)











 #funtion for help commands

@bot.message_handler(commands=["help"])
def help_command(message):
    print("help command selected")
    help_text = "This bot is a Gaming company called Manzium bot. NB: This bot will help you know more about games and some equippment for game"
    bot.reply_to(message, help_text)



@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    if "hi" in message.text:
        bot.reply_to(message, "Hello there")
    elif "good morning" in text:
        bot.reply_to(message, " The morning is good")
    elif "how are you" in text:
        bot.reply_to(message, "I am very good")
    elif "task" in text:
        bot.reply_to(message, "Please wait for a minute")
    elif "account" in text:
        bot.reply_to(message, "Analzing data info...")
    # elif "bloxfruits stock" in text:
    #     bot.reply_to(message, "Bloxfruits Stock: \n"
    #                           "Magma \n"
    #                           "Rubber \n"
    #                           "Control \n"
    #                           "Diamond \n"
    #                           "Chop \n")
    # elif "game recommendation" in text:
    #     bot.reply_to(message, "Please wait for a minute \n"
    #                           "Bloxfruit \n"
    #                           "Fortnite \n"
    #                           "Call Off Duty \n"
    #                           "Asphalt 8 \n")
    # elif "game puzzle" in text:
    #     bot.reply_to(message, " What game puzzle would you like to solve")
    # elif "gamedata" in text:
    #     bot.reply_to(message, " Let me check your gamedata so far: \n"
    #                           "In bloxfruits: you are level 1772, you have spirit and control in stock, you have 117 bones \n"
    #                           "In Fortnite: you are level 13, you have 1 skin and 2 guns \n")

    else:
        bot.reply_to(message, "I dont understand")

    print_user_info(message.from_user, message.text)

def print_user_info(user, message_text):
    if user.username:
        if user.username:
            print(f"Username: @{user.username} sent: {message_text}")
        elif user.first_name:
            print(f"First Name: {user.first_name} sent: {message_text}")










print("Bot is starting ...")
bot.polling()
