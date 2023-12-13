"""
Author: Team Messi
Group members:
            Elinam Kodea
            Monalisa Afodour
            Nana Osei Opoku-Sarkodie
            Kofi Asante
            Ronny Tay
            Josephine Mensah
Date: 2nd November 2023.
Description: A bot to help you order pizza at a pizza restaurant
Step 1: Use the terminal to run "pip install pyTelegramBotAPI"
"""




import telebot #improts the telebot library
TOKEN = "YOUR_TOKEN" # token to access telebot
bot = telebot.TeleBot(TOKEN)  # registers the bot



#function for all keyboards
def start_keyboard(): #keyboard for start
    #create an object for the keyboardmarkup()
    start_kb = telebot.types.InlineKeyboardMarkup()
    start_kb.row(telebot.types.InlineKeyboardButton("Poor Customer Service", callback_data="poor"),
                 telebot.types.InlineKeyboardButton("About Food", callback_data="food"))
    start_kb.row(telebot.types.InlineKeyboardButton("About Waiter", callback_data="waiter"),
                 telebot.types.InlineKeyboardButton("About Restaurant", callback_data="restaurant"))


    return start_kb


def food_keyboard(): #for food
    #create an object for the keyboardmarkup()
    food_kb = telebot.types.InlineKeyboardMarkup()
    food_kb.row(telebot.types.InlineKeyboardButton("Food Not Hot", callback_data="hotness"),
                telebot.types.InlineKeyboardButton("Foreign Material in Food", callback_data="foreign"))
    food_kb.row(telebot.types.InlineKeyboardButton("Wrong Order", callback_data="wrong"))

    return food_kb






def waiter_keyboard():
    #create an object for the keyboardmarkup()
    waiter_kb = telebot.types.InlineKeyboardMarkup()
    waiter_kb.row(telebot.types.InlineKeyboardButton("Rude Attitude", callback_data="attitude"),
                telebot.types.InlineKeyboardButton("Slow Service", callback_data="slow"))
    waiter_kb.row(telebot.types.InlineKeyboardButton("Mistakes With Orders", callback_data="mistakes"))

    return waiter_kb




def restaurant_keyboard():
    #create an object for the keyboardmarkup()
    restaurant_kb = telebot.types.InlineKeyboardMarkup()
    restaurant_kb.row(telebot.types.InlineKeyboardButton("Too Dirty", callback_data="dirty"),
                telebot.types.InlineKeyboardButton("Bad Odour", callback_data="odour"))
    restaurant_kb.row(telebot.types.InlineKeyboardButton("Pest", callback_data="pest"))

    return restaurant_kb

def choice_keyboard():
    choice_kb = telebot.types.InlineKeyboardMarkup()
    choice_kb.row(telebot.types.InlineKeyboardButton("Yes", callback_data="yes"),
                  telebot.types.InlineKeyboardButton("No", callback_data="no"))
    return choice_kb


def poor_keyboard():
    #create an object for the keyboardmarkup()
    poor_kb = telebot.types.InlineKeyboardMarkup()
    poor_kb.row(telebot.types.InlineKeyboardButton("Ineffective Communication", callback_data="communication"),
                  telebot.types.InlineKeyboardButton("Lack of Training and Knowledge", callback_data="training"))
    poor_kb.row(telebot.types.InlineKeyboardButton("Long Wait Times and Delays", callback_data="delays"))

    return poor_kb

















#end of function of all keyboards

#functions for callback
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == "poor":
        print("poor selected")
        poor_text = "Please select one of the following options." #change question
        bot.send_message(call.message.chat.id, poor_text, reply_markup=poor_keyboard())

    elif call.data == "food":
        print("Food selected")
        food_text = "Please select one of the following choices: " #change question
        bot.send_message(call.message.chat.id, food_text, reply_markup= food_keyboard())

    elif call.data == "waiter":
        print("waiter selected")
        waiter_text = "State your complaint against our waiter: " #change question
        bot.send_message(call.message.chat.id, waiter_text, reply_markup= waiter_keyboard())

    elif call.data == "restaurant":
        print("restaurant selected")
        restaurant_text = "Please state your complaints about our restaurant: " #change question
        bot.send_message(call.message.chat.id, restaurant_text, reply_markup= restaurant_keyboard())

    elif call.data == "hotness":
        print("hotness selected")
        hotness_text = ("We are so sorry to hear that your food is not hot. We will be\n"
                     "warming it for you right way.") #change question
        bot.send_message(call.message.chat.id, hotness_text)

    elif call.data == "no":  # change callback
        print("No selected")  # change string
        no_text = "Sorry for the inconvenience. We will be replacing your order."  # change question
        bot.send_message(call.message.chat.id, no_text)

    elif call.data == "yes":  # change callback
        print("yes selected")  # change string
        yes_text = "Your refund is being processed"  # change question
        bot.send_message(call.message.chat.id, yes_text)

    elif call.data == "communication":
        print("communication selected")
        communication_text = "We will try to communicate our ideas to you much clearly"
        bot.send_message(call.message.chat.id, communication_text)

    elif call.data == "delays":
        print("delays selected")
        delays_text = ("We will speak with our waiters and staff to deliver your orders as quick as possible. \n"
                       "Thank you for your patience with us")
        bot.send_message(call.message.chat.id, delays_text)

    elif call.data == "training":
        print("training selected")
        training_text = ("Sorry that you had to deal with this issue. We will be more mindful of the kind of training we give to our staff.")
        bot.send_message(call.message.chat.id, training_text)

    elif call.data == "foreign":
        print("foreign selected")
        foreign_text = "Do you want a refund?"
        bot.send_message(call.message.chat.id, foreign_text, reply_markup=choice_keyboard())

    elif call.data == "dirty":
        print("dirty selected")
        dirty_text = ("Sorry for such a misfortune. We will speak with out \n"
                     "cleaners so that you do not have to deal with this again.")
        bot.send_message(call.message.chat.id, dirty_text)

    elif call.data == "odour":
        print("odour selected")
        odour_text = ("We will do our best to make sure that the odour in our infrastructure is tolerable.")
        bot.send_message(call.message.chat.id, odour_text)

    elif call.data == "wrong":
        print("wrong selected")
        wrong_text = ("Sorry for such a mistake. We will return to you with the correct order.")
        bot.send_message(call.message.chat.id, wrong_text)

    elif call.data == "pest":
        print("pest selected")
        pest_text = ("We will do our best to get rid of the pests you have detected in our establishment. Thank you for bringing this to our attention!")
        bot.send_message(call.message.chat.id, pest_text)

    elif call.data == "attitude":
        print("attitude selected")
        attitude_text = ("We apologise for this occurance. Please bear with us as we resolve the issue.")
        bot.send_message(call.message.chat.id, attitude_text)

    elif call.data == "mistakes":
        print("mistakes selected")
        mistakes_text = ("Sorry for the inconvenience. You would be receiving your correct order soon.")
        bot.send_message(call.message.chat.id, mistakes_text)

    elif call.data == "slow":
        print("slow selected")
        slow_text = ("Your orders would be delivered as fast as you wold like it to. Thank you for your understanding.")
        bot.send_message(call.message.chat.id, slow_text)




#end of functions for callback







#Command functions
#function for start command
@bot.message_handler(commands=["start"])
def start_messsage(message):
    print("start command selected")
    #String for message text
    message_text = ("Welcome to Messi's pizza, an A-class restaurant here to give you the best customer service and to \n"
                    "provide the best quality pizza for all our customers. This chatbot is designed to aid you in \n"
                    "ordering the city's best pizza right here in Messi's Pizza. Please select one of the following.")
    bot.reply_to(message, message_text, reply_markup=start_keyboard())









@bot.message_handler(commands=["members"])
def group_members(message):
    print("Member command selected")
    members_text = ("This bot was developed by Mercy's pizza: \n"
                    "Monalisa \n"
                    "Nana Osei \n"
                    "Kofi Asante \n"
                    "Elinam \n"
                    "Ronny \n"
                    "Josephine")
    bot.reply_to(message, members_text)


@bot.message_handler(commands=["help"])
def help_command(message):
    print("help command selected")
    help_text = ("This bot is for a pizza restuarant called 'Mercy's Pizza'. It was made to help customers order "
                 "pizza easily and effectively 👍👍.")
    bot.reply_to(message, help_text)



@bot.message_handler(func=lambda message: True)
def handle_message(message): # parameter
    text = message.text.lower() #changes the message text to lower case
    #selection statement
    if "hi" in text: #use the message.text function

        bot.reply_to(message, "Hello there!") #argument
    elif "good morning" in text:
        bot.reply_to(message, "Morning good")
    elif "how are you" in text:
        bot.reply_to(message, "I am doing very great.")
    elif "Say something funny" in text:
        bot.reply_to(message, "What do you call a sleeping buffalo? A bulldozer!")
    elif "Yo" in text:
        bot.reply_to(message, "Cool.")
    elif "Wassup" in text:
        bot.reply_to(message, "I'm chill. You?")
    elif "Messi is the GOAT!" in text:
        bot.reply_to(message, "YESSSIR! HE IS.")
    elif "Is Ronaldo the GOAT" in text:
        bot.reply_to(message, "NAH. NOT IN A MILLION YEARS.")
    elif "Do you love me?" in text:
        bot.reply_to(message, "I am a bot. I do not persue emotional pleasure.")
    elif "Do you want to be my friend" in text:
        bot.reply_to(message, "Yes I will like to be your friend.")
    elif "How much food can I eat today" in text:
        bot.reply_to(message, "You can eat as much as you want.")
    elif "What is your purpose" in text:
        bot.reply_to(message, "I am a chatbot designed to provide you with the best customer service as you\n"
                              "come here to order.")
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
