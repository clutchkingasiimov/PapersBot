from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#Updater method
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

text = """Hello there! Welcome to PapersBot, a easy to use bot for scanning latest updates on
research articles from curated list of Elsevier and Wiley.

Before we begin, what may I call you as?"""

#Basic messaging func (Callback function)
def start_message(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
	                         text=text)


# echo_handler = MessageHandler(Filters.text, echo) #Responds to the messages
# dispatcher.add_handler(echo_handler)

start_handler = CommandHandler('start', start_message) #Responds to commands
dispatcher.add_handler(start_handler)

poppin_handler = CommandHandler('wassup', wus_poppin)
dispatcher.add_handler(poppin_handler)
updater.start_polling()


