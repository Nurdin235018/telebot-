from telebot import TeleBot 
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from decouple import config

token = config('TOKEN')

bot = TeleBot(token)

@bot.message_handler(['start', 'stop', 'fact'])
def start_message(message: Message):
    bot.send_message(message.chat.id, f'Hello {message.chat.username}')


@bot.message_handler(func=lambda message: message.text == 'buttons')
def get_buttons(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('button1')
    button2 = KeyboardButton('button2')
    keyboard.add(button1, button2)

    bot.send_message(message.chat.id, "Click me", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'button1')
def inline_buttons(message:Message):
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('hello', callback_data='call1')
    button2 = InlineKeyboardButton('goodbye', callback_data='call2')
    keyboard.add(button1, button2)

    bot.reply_to(message, 'take buttons in message', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda c: True)
def handle_callback_data(callback: CallbackQuery):
    if callback.data == 'call1':
        bot.send_sticker(callback.message.chat.id, sticker='CAACAgIAAxkBAAEJ93Fk05c5pwqfRHMr_nABZaxEQPQiSAAC_xAAApc0QEukJ1CkXhMnSDAE')
    else:
        bot.send_sticker(callback.message.chat.id, sticker='CAACAgIAAxkBAAEJ92pk05cZS2autVDCoBKazpSXfb9aVgACwxAAAssumElkZuP-rXcveDAE')


bot.infinity_polling()
