# Importing modules and file with token
import telebot
import random
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_message(message):
    mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nЯ бот"
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['github'])
def github(message):
    mess = f"<b>Вот GitHub моего создателя</b>!\nhttps://github.com/geoking1907"
    bot.send_message(message.chat.id, mess, parse_mode='html')

    
# All photos are in my computer
@bot.message_handler(commands=['photo'])
def func(message):
    a = str(random.randint(1, 27))
    photo = open('img\i ({}).jpg'.format(a), 'rb')
    bot.send_photo(message.chat.id, photo)
    
    
bot.polling()
