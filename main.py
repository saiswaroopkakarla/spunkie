#!/usr/bin/env python
# coding: utf-8

# In[9]:


from telegram import *
from telegram.ext import *
bot = Bot("1976152623:AAEWwWiH0klhAJdnUDFiP5gXiUNNc4ahTbk")
print(bot.get_me())
updater=Updater("1976152623:AAEWwWiH0klhAJdnUDFiP5gXiUNNc4ahTbk",use_context=True)
dispatcher=updater.dispatcher

def doTheFlames(update:Update,context:CallbackContext):
    bot.send_message(
    chat_id=update.effective_chat.id,
    text="bot is working")

def reply(update:Update,context:CallbackContext):
    bot.send_message(
    chat_id=update.effective_chat.id,
    text="Your message is: " +update.message.text + "./n please send proper names")


start_value=CommandHandler("flames",doTheFlames)

couple_name= MessageHandler(Filters.text, reply)

dispatcher.add_handler(start_value)

dispatcher.add_handler(couple_name)

updater.start_polling()
