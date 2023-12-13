"""
Author:
Benjamin Abbey
Welch Appiah
Benjamin Gakpe
Daniel Gyamfi

Bot Username: @fatherblack2_bot
Date: 20th October, 2023.
Descriptions : Testing telegram bot using Python language.
Step 1: Install pyTelegramBotAPI using pop install pyTelegramBotAPI
Step 2: Import telegram
Step 3: Register your telegram token using telebot.TeleBot(TOKEN)

"""

import telebot  #imports the telegram library
TOKEN = "YOUR_TOKEN"
bot = telebot.TeleBot(TOKEN) #registers the bot

#function for all keyboards
def start_keyboard():
    #create an obeject for the keyboardmarkup()
    start_kb = telebot.types.InlineKeyboardMarkup()
    start_kb.row(telebot.types.InlineKeyboardButton("Catalogue of books ", callback_data="catalogue"),
                telebot.types.InlineKeyboardButton("Pending order", callback_data="pending"))
    start_kb.row(telebot.types.InlineKeyboardButton("Report and issue", callback_data="report"))
    return  start_kb


def report_keyboard(): # this callback if for reporting an issue
    #create an obeject for the keyboardmarkup()
    report_kb = telebot.types.InlineKeyboardMarkup()
    report_kb.row(telebot.types.InlineKeyboardButton("Wrong order", callback_data="wrong"),
                 telebot.types.InlineKeyboardButton("Missing pages", callback_data="missing"))
    return report_kb



def catalogue_keyboard():
    #create an obeject for the keyboardmarkup()
    catalogue_kb = telebot.types.InlineKeyboardMarkup()
    catalogue_kb.row(telebot.types.InlineKeyboardButton("Horror", callback_data="horror"),
                 telebot.types.InlineKeyboardButton("Comic", callback_data="comic"))
    catalogue_kb.row(telebot.types.InlineKeyboardButton("classic", callback_data="classic"),
                telebot.types.InlineKeyboardButton("Fantasy", callback_data="fantasy"))
    return catalogue_kb


def option_keyboard():
    #create ana object for the keyboardmarkup()
    option_kb = telebot.types.InlineKeyboardMarkup()
    option_kb.row(telebot.types.InlineKeyboardButton("Yes", callback_data="yes"),
                telebot.types.InlineKeyboardButton("No", callback_data="no"))
    return option_kb

def types_keyboard():
    #create an obeject for the keyboardmarkup()
    types_kb = telebot.types.InlineKeyboardMarkup()
    types_kb.row(telebot.types.InlineKeyboardButton("Dracula", callback_data="dracula"),
                 telebot.types.InlineKeyboardButton("I.T", callback_data="IT"))
    types_kb.row(telebot.types.InlineKeyboardButton("Ghost Story", callback_data="ghost story"),
                 telebot.types.InlineKeyboardButton("Frankenstein", callback_data="frankenstein"))
    return types_kb

def kind_keyboard():
    #create an obeject for the keyboardmarkup()
    kind_kb = telebot.types.InlineKeyboardMarkup()
    kind_kb.row(telebot.types.InlineKeyboardButton("Flash", callback_data="flash"),
                 telebot.types.InlineKeyboardButton("Superman", callback_data="superman"))
    kind_kb.row(telebot.types.InlineKeyboardButton("Batman", callback_data="batman"))
    return kind_kb

def sort_keyboard():
    #create an object for the keyboardmarkup()
    sort_kb = telebot.types.InlineKeyboardMarkup()
    sort_kb.row(telebot.types.InlineKeyboardButton("The catcher in the rye", callback_data="catcher"),
                 telebot.types.InlineKeyboardButton("Ninteen Eighty-four", callback_data="eighty four"))
    sort_kb.row(telebot.types.InlineKeyboardButton("Bridesshead Revisited", callback_data="revisited"))
    return sort_kb


def category_keyboard():
    #create an obeject for the keyboardmarkup()
    category_kb = telebot.types.InlineKeyboardMarkup()
    category_kb.row(telebot.types.InlineKeyboardButton("Hobbit", callback_data="hobbit"),
                 telebot.types.InlineKeyboardButton("The name of the wind", callback_data="wind"))
    category_kb.row(telebot.types.InlineKeyboardButton("Alice in wonderland", callback_data="alice"))
    return category_kb
#end of function

#function for callback

#The function below handles all keyboards selection or callback data
@bot.callback_query_handler(func=lambda call: True)
def handler_callback_query(call): #handles all keyboard responses
    #option when imperfect is selected
    if call.data == "report": #change callback
        print("Report an issue selected")#change string
        report_text = "Please select one of the following "#change question
        bot.send_message(call.message.chat.id,report_text, reply_markup=report_keyboard())
        #calls the product_keyboard function to draw the keyboard



    elif call.data == "catalogue":#change callback
        print("catalogue selected")  # change string
        catalogue_text = "What type of books are you looking for?"  # change question
        bot.send_message(call.message.chat.id, catalogue_text, reply_markup=catalogue_keyboard())

    elif call.data == "pending":#change callback
        print("Pending selected")  # change string
        pending_text = "Sorry for the inconvenience, your missing items would be sent to you at no cost."  # change question
        bot.send_message(call.message.chat.id, pending_text)
    #end of main meny keyboard responses

    #start of main menu keyboard responses
    elif call.data == "yes":  # change callback
        print("Yes selected")  # change string
        yes_text = "refund in process."  # change question
        bot.send_message(call.message.chat.id, yes_text)

    elif (call.data == "wrong") or (call.data == "missing"):  # change callback
        print("wrong or missing selected")  # change string
        wrong_text = "Do you want a refund?" # change question
        bot.send_message(call.message.chat.id, wrong_text, reply_markup=option_keyboard())

    elif call.data == "dracula": #change callback
        print("Dracula selected")  # change string
        dracula_text = "This is a customers favourite which is issued at $29.99."  # change question
        bot.send_message(call.message.chat.id, dracula_text)

    elif call.data == "frankenstein": #change callback
        print("Frankenstein selected")  # change string
        frankenstein_text = "This is a customers favourite which is issued at $29.99."  # change question
        bot.send_message(call.message.chat.id, frankenstein_text)

    elif call.data == "IT": #change callback
        print("IT selected")  # change string
        IT_text = "This captivating book is available for just $29.99"  # change question
        bot.send_message(call.message.chat.id, IT_text)

    elif call.data == "ghost story":
        print("Ghost story selected")
        ghost_story_text = "Experience the magic of this captivating book, now within your reach for just $29.99."
        bot.send_message(call.message.chat.id, ghost_story_text)

    elif call.data == "flash":
        print("Flash selected")
        flash_text = "This is a fascinating book going for $29.99"
        bot.send_message(call.message.chat.id, flash_text)

    elif call.data =="superman":
        print("Superman selected")
        superman_text = "This is a engaging book going for $29.99"
        bot.send_message(call.message.chat.id, superman_text)

    elif call.data == "batman":
        print("Batman selected")
        batman_text = "This is an interesting book going for $29.99"
        bot.send_message(call.message.chat.id, batman_text)

    elif call.data == "catcher":
        print("The catcher in the rye selected")
        catcher_text = "This is an interesting book going for $29.99"
        bot.send_message(call.message.chat.id, catcher_text)

    elif call.data == "eighty four":
        print("Ninteen-eighty four  selected")
        eighty_four_text = "This is an interesting book going for $29.99"
        bot.send_message(call.message.chat.id, eighty_four_text)

    elif call.data == "revisited":
        print("Bridesshead Reivisited")
        revisited_text = "This is an enjoyable book going for $29.99"
        bot.send_message(call.message.chat.id, revisited_text)

    elif call.data == "hobbit":
        print("Hobbit")
        hobbit_text = "This is an interesting book going for $29.99"
        bot.send_message(call.message.chat.id, hobbit_text)


    elif call.data == "wind":
        print("The name of the wind")
        wind_text = "This is an engaging book going for $29.99"
        bot.send_message(call.message.chat.id, wind_text)

    elif call.data == "alice":
        print("Alice in wonderland")
        alice_text = "This is an interesting book going for $29.99"
        bot.send_message(call.message.chat.id, alice_text)

    elif call.data == "no":#change callback
        print("No selected")  # change string
        no_text = "Sorry for the inconvenience."  # change question
        bot.send_message(call.message.chat.id, no_text)

    elif call.data == "horror":#change callback
        print("horror selected")  # change string
        horror_text = "The horror books available are"  # change question
        bot.send_message(call.message.chat.id, horror_text, reply_markup=types_keyboard())

    elif call.data == "comic":#change callback
        print("comic selected")  # change string
        comic_text = "The comic books available are"  # change question
        bot.send_message(call.message.chat.id, comic_text, reply_markup=kind_keyboard())

    elif call.data == "classic":#change callback
        print("classic selected")  # change string
        classic_text = "The classic books available are"  # change question
        bot.send_message(call.message.chat.id, classic_text, reply_markup=sort_keyboard())

    elif call.data == "fantasy":#change callback
        print("fantasy selected")  # change string
        fantasy_text = "The fantasy books available are"  # change question
        bot.send_message(call.message.chat.id, fantasy_text, reply_markup=category_keyboard())






#function for start command

@bot.message_handler(commands=["start"])
def start_message(message):
    print("start command selected")
    message_text= ("Welcome to Father Black's Book Store, an imaginary book store where "
                   "stories come alive."
                   " \n Please select one of the following")
    bot.reply_to(message,message_text, reply_markup=start_keyboard()) #for reply to command


# a function to handle the members command
@bot.message_handler(commands=["members"])
def  group_members(message):
    print("Members command selected")
    members_text = ("This bot was developed by Father Black Book Inc: \n"
                    "Abbey \n" #\n sends the text to the next line 
                    "Gakpe \n"
                    "Jayden \n"
                    "Daniel \n"
                    "Welch")
    bot.reply_to(message, members_text)



@bot.message_handler(commands=["help"])
def help_command(message):
    print("help command selected")
    help_text = ("This bot is used to recommend books on specific aspects of Black fatherhood.")
    bot.reply_to(message, help_text)

#function to handle bot chatting.
@bot.message_handler(func=lambda message : True)
def handle_message(message): #anything in the bracket is a parameter
    text = message.text.lower()#changes message text to lower case
    #selection statement
    if "hi" in text:

        bot.reply_to(message, "Hello there, how can i assist you? ") #arguement
    elif "good morning" in text:
        bot.reply_to(message, "The morning is good.")
    elif "hello" in text:
        bot.reply_to(message, "Hello there, how can i assist you? ")
    elif "hey" in text:
        bot.reply_to(message, "Hello there, how can i assist you? ")
    elif "your use" in text:
        bot.reply_to(message, "I provide customer service support for Father Black Books.")
    elif "name" in text:
        bot.reply_to(message, "My name is Father Black's bot!  How can I help you today?")
    elif "how you" in text:
        bot.reply_to(message, "I am functioning as intended.")
    elif "good evening" in text:
        bot.reply_to(message, "The evening is good.")
    elif "good afternoon" in text:
        bot.reply_to(message, "The afternoon is good.")
    elif "joke" in text:
        bot.reply_to(message, "Why did the book go to the doctor? Because it had too many paper cuts!")
    elif "order a book" in text:
        bot.reply_to(message, "Kindly type /start to get a drop down menu to order.")
    elif "type of books" in text:
        bot.reply_to(message, "Kindly type /start to find out.")
    elif "problem with book" in text:
        bot.reply_to(message, "Type /start and select  report and issue")
    elif "not arrived" in text:
        bot.reply_to(message, "Kindly type /start and tap on the pending order")
    elif "night" in text:
        bot.reply_to(message, "The night is good")
    elif "bye" in text:
        bot.reply_to(message, "Bye, we look forward to hearing you soon")
        
    else:
        bot.reply_to(message, "I don't understand")

    #this prints our the message sent and the user
    print_user_info(message.from_user, message.text)

def print_user_info(user, message_text): #function to print out the data of user in the console
    if user.username:
        print(f"Username: @{user.username} sent: {message_text}")
    elif user.first_name:
        print(f"First Name: {user.first_name} sent: {message_text}")









print("Bot is starting...")
bot.polling()#starts the bot
