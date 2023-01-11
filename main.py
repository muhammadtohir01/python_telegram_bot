from telegram import Bot
import os

# get token from env
TOKEN = os.environ['TOKEN']
# Create a bot object
bot = Bot(token=TOKEN)

chat_id =5575549228
# Send message
bot.sendMessage(chat_id=chat_id,text='Salom')

# Get updates from bot

updates = bot.getUpdates()
photos = updates[5].message.photo
file_id=photos[0].file_id
print(file_id)
bot.sendPhoto(chat_id=chat_id,photo=file_id)
