from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters
from telegram import Update
import os

# get token from env
TOKEN = os.environ['TOKEN']

def start(update: Update, context: CallbackContext):
    print('Start command')

def echo(update: Update, context: CallbackContext):
    print('Echo')

updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()