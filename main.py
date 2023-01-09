from telegram import Bot
import os

# get token from env
TOKEN = os.environ['TOKEN']
# Create a bot object
bot = Bot(token=TOKEN)
# Print bot info
x=bot.getMe()
print(x.id)
print(x.first_name)
