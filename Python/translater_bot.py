# Bismillah
"""
Created on Tue Jul  9 18:02:51 2024

@author: Faxriddin
"""

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = "7351000201:AAGDZ0Q6xMu97u686xk6iGlH96hnCBrIvG8"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum, Xush kelibsiz!"
    javob += "\nMatn kiriting: "
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    # if msg.isascii():
    #     javob = to_cyrillic(msg)
    # else:
    #     javob = to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.infinity_polling()

# matn = input("Matn kiriting: ")

# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))