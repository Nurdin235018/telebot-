import requests
from telebot import types as t
from telebot import TeleBot 
from decouple import config 

token = config('TOKIN')
bot = TeleBot(token)

def get_fact():
    url = 'https://catfact.ninja/fact'
    fact = requests.get(url)
    return fact.json()['fact']


@bot.message_handler(['start', 'fact'])
def send_fact(message: t.Message):
    bot.reply_to(message,get_fact())


bot.infinity_polling()