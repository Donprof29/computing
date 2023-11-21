'''
Author: Team Fedora
Group Members:
            Kofi Asante
            Nana Osei
            Abbey
Date: 2nd November, 2023.
Description: A bot to help you purchase a game

Step 1: Use =the terminal to run "pip install pyTelegramBotAPI"

'''

import telebot  #imports the telebot library
TOKEN = "REPLACE_TOKEN"
bot = telebot.TeleBot(TOKEN)  # registers the bot


#function for all keyboards
def start_keyboard():
    #create an object for the keyboardmarkup()
    start_kb = telebot.types.InlineKeyboardMarkup()
    start_kb.row(telebot.types.InlineKeyboardButton("Product & Service", callback_data="product"),
                 telebot.types.InlineKeyboardButton("Pricing and Packages", callback_data="pricing"))

    start_kb.row(telebot.types.InlineKeyboardButton("Technical Support",callback_data="technical"))
    return start_kb


def product_keyboard():
    #create an object for the keyboardmarkup()
    product_kb = telebot.types.InlineKeyboardMarkup()
    product_kb.row(telebot.types.InlineKeyboardButton("Software solutions", callback_data="software"),
                 telebot.types.InlineKeyboardButton("Cloud Computing", callback_data="cloud"))

    product_kb.row(telebot.types.InlineKeyboardButton("Cybersecurity",callback_data="cyber"))
    return product_kb


#end of function of all keyboards


#start of call back functions
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call): #handles all keyboard responses
    if call.data == "product":
        print("Product selected")
        product_text = "Which area are you interested in?"
        bot.send_message(call.message.chat.id, product_text, reply_markup=product_keyboard())



# function for start command
@bot.message_handler(commands=["start"])
def start_message(message):
    print("start command selected")
    #String for message text
    message_text = ("Welcome to Bit Cloud, an imaginary IT solutions"
                    "company, we aim to enhance our customer services"
                    "capabilities by developing an interactive chatbot."
                    "This chatbot is developed to guide clients through"
                    "their inquiries.\n Please select one"
                    "of the following.")
    bot.reply_to(message, message_text, reply_markup=start_keyboard())








@bot.message_handler(commands=["members"])
def group_members(message):
    print("Member command selected")
    members_text = ("This bot was developed by Father Black Book Inc: \n"
                    "Don Prof \n"
                    "Osei Sark \n"
                    "Elinam \n"
                    "Kofi Asante \n"
                    "Macario \n"
                    "Ron \n"
                    "Jose")
    bot.reply_to(message, members_text)

# function for help command
@bot.message_handler(commands=["help"])
def help_command(message):
    print("help command selected")
    help_text = ("This bot is for an imaginary company "
                 "called Bit Cloud. NB: The bot was designed"
                 "solely for academic purposes only.")
    bot.reply_to(message, help_text)



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
