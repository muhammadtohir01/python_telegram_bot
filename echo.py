from telegram.ext import Updater,CommandHandler,CallbackContext
from telegram import Update
import os

# get token from env
TOKEN = os.environ['TOKEN']

def start(update: Update, context: CallbackContext):
    print('Work')


updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))

updater.start_polling()
updater.idle()