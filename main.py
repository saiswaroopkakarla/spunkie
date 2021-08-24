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
    if __name__ == "__main__" :
        Firstname,Secondname=update.message.text.split("/")
        p1 = Firstname
 
    # converted all letters into lower case
        p1 = p1.lower()
 
    # replace any space with empty string
        p1.replace(" ", "")
 
    # make a list of letters or characters
        p1_list = list(p1)
 
    # take 2nd name
        p2 = Secondname
        p2 = p2.lower()
        p2.replace(" ", "")
        p2_list = list(p2)
 
    # taking a flag as True initially
        proceed = True
     
    # keep calling remove_match_char function
    # until common characters is found or
    # keep looping until proceed flag is True
        while proceed :
            ret_list = remove_match_char(p1_list, p2_list)
 
        # take out concatenated list from return list
            con_list = ret_list[0]
 
        # take out flag value from return list
            proceed = ret_list[1]
 
        # find the index of "*" / border mark
            star_index = con_list.index("*")
 
        # list slicing perform
         
        # all characters before * store in p1_list
            p1_list = con_list[ : star_index]
 
        # all characters after * store in p2_list
            p2_list = con_list[star_index + 1 : ]
 
 
    # count total remaining characters
        count = len(p1_list) + len(p2_list)
 
    # list of FLAMES acronym
        result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
 
    # keep looping until only one item
    # is not remaining in the result list
        while len(result) > 1 :
 
        # store that index value from
        # where we have to perform slicing.
            split_index = (count % len(result) - 1)
 
        # this steps is done for performing
        # anticlock-wise circular fashion counting.
            if split_index >= 0 :
 
            # list slicing
                right = result[split_index + 1 : ]
                left = result[ : split_index]
 
            # list concatenation
                result = right + left
 
            else :
                result = result[ : len(result) - 1]
 
       # print final result
        
        bot.send_message(
        chat_id=update.effective_chat.id,
        text="Relationship status :"+ result[0])

def reply(update:Update,context:CallbackContext):
    bot.send_message(
    chat_id=update.effective_chat.id,
    text="Please enter Your Name/YourCrush's Name. For ex: Ramaraju/Priya rani")

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

 #code for flames
def remove_match_char(list1, list2):
 
    for i in range(len(list1)) :
        for j in range(len(list2)) :
 
            # if common character is found
            # then remove that character
            # and return list of concatenated
            # list with True Flag
            if list1[i] == list2[j] :
                c = list1[i]
 
                # remove character from the list
                list1.remove(c)
                list2.remove(c)
 
                # concatenation of two list elements with *
                # * is act as border mark here
                list3 = list1 + ["*"] + list2
 
                # return the concatenated list with True flag
                return [list3, True]
 
    # no common characters is found
    # return the concatenated list with False flag
    list3 = list1 + ["*"] + list2
    return [list3, False]

dispatcher.add_handler(CommandHandler("start", start))

start_value=CommandHandler("flames",reply)

couple_name= MessageHandler(Filters.text, doTheFlames)

dispatcher.add_handler(start_value)

dispatcher.add_handler(couple_name)


updater.start_polling()
