import requests
import telebot
from telebot.types import Message
import random




TOKEN = '1163401195:AAHf8Cpgjeysp-FNqzJ_zmQrkLlmXXJf1Es'
STICKER_ID = 'CAACAgIAAxkBAAOFXrgQOdQbbCOKqfiBWg8WD5c8l44AAgoAA8A2TxP_Da4-6A79CBkE'
photo = open('C:/Users/Михаил/Desktop/vansi_for_dimas.jpg', 'rb')
bot = telebot.TeleBot(TOKEN)
users_list = []


@bot.message_handler(commands=['start'])
def command_handler(message: Message):
    bot.reply_to(message, 'Стартуем ибо пиздуем')

@bot.message_handler(commands=['help'])
def command_handler(message: Message):
    bot.reply_to(message, 'Хелпуем ибо пиздуем')

@bot.message_handler(commands=['photo'])
def photo_handler(message: Message):
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message: Message):
    if 'тачка' in message.text:
        bot.reply_to(message, 'Тачка не лох, а Дима лох')
        return
    reply = 'Врум врум врум в бошке лишь арматура'
    if message.from_user.id in users_list:
        reply += ", привет еще раз!"
    bot.reply_to(message, reply)
    users_list.append((message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username))
    print(users_list)

@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.send_sticker(message.chat.id, STICKER_ID)




bot.polling()


