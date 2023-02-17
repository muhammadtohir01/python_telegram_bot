from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters
from telegram import Update,ReplyKeyboardMarkup
import os

TOKEN = os.environ['TOKEN']

def start(update: Update, context: CallbackContext):
    markup = ReplyKeyboardMarkup(
        [['Cheese Burger','Gam Burger'],
           ['Lavash','Xot Dog'] ]
        )
    bot = context.bot
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id,'Assalom alaykum xush kelibsiz botimizga 👍 \
        \nFastfood munyularimiz bilan quyidagi buttonlar orqali tanishining 👇', reply_markup=markup)

# menyular turlari
def Lavash(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    bot = context.bot
    markum=ReplyKeyboardMarkup(
        [['Chikkenli','tovuqli'],
           ['Burdali','Qiymali'],
           ["Buyurtma"]
           ])
    bot.sendMessage(chat_id,'Lavash turlari👇', reply_markup=markum)

def CheeseBurger(update:Update,context:CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    markup=ReplyKeyboardMarkup([
        ['Bar bique burger','Chikkenli'],
         ["Buyurtma"]
    ])
    bot.sendMessage(chat_id,'CheeseBurger turlari👇',reply_markup=markup)

def GamBurger(update: Update, context: CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    markup=ReplyKeyboardMarkup([
        ["Qo'y go'shli","Mol go'shli"],
        ["Buyurtma"]
    ])
    bot.sendMessage(chat_id,"GamBurger turlari👇",reply_markup=markup)

def XotDog(update: Update, context: CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    markup=ReplyKeyboardMarkup([
        ["Lepo'shkali","Pitali"],
        ["Buyurtma"]
    ])
    bot.sendMessage(chat_id,"XotDog turlari👇",reply_markup=markup)

def Buyurtma(update: Update, context: CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    markup=ReplyKeyboardMarkup([
        ["Lacation","Nomer"]
    ])
    bot.sendMessage(chat_id,'Buyurtma berish👇',reply_markup=markup)
def Location(update: Update, context: CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    latitude=39.661211
    longitude=67.010697

    param={
            'chat_id':chat_id,
            'latitude':latitude,
            'longitude':longitude
        }
    bot.sendMessage(chat_id,'Location',location=param)

# def Buyurtma(update: Update, context: CallbackContext):
#     chat_id=update.message.chat.id
#     bot=context.bot

updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Lavash'),Lavash))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Cheese Burger'), CheeseBurger))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Gam Burger'), GamBurger))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Xot Dog'), XotDog))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Buyurtma'),Buyurtma))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Location'),Location))
updater.start_polling()
updater.idle()