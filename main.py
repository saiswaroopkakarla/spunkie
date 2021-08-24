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
    bot.send_message("okok")

start_value=CommandHandler("flames",doTheFlames)


# In[ ]:




