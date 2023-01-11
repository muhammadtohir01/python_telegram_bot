from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters
from telegram import Update
import os

# get token from env
TOKEN = os.environ['TOKEN']

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    bot = context.bot
    bot.sendMessage(chat_id,'Assalom alaykum xush kelibsiz botimizga 👍')

def echo(update: Update, context: CallbackContext):
    # Get text from update
    text = update.message.text
    chat_id = update.message.chat.id
    print(text)
    # Send message to Bot
    bot = context.bot
    bot.sendMessage(chat_id,text)

def hi(update: Update, context: CallbackContext):
    print('hi')
    chat_id = update.message.chat.id

    bot = context.bot
    bot.sendMessage(chat_id,'Salom')

def help(update: Update, context: CallbackContext):
    print('hi')
    chat_id = update.message.chat.id

    bot = context.bot
    bot.sendMessage(chat_id,'Qanday yordam kerak!!!')
updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(CommandHandler('help',help))
updater.dispatcher.add_handler(MessageHandler(Filters.text('hi'),hi))
updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()