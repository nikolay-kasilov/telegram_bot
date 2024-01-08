import telebot

from telebot import types
bot = telebot.TeleBot('6874199225:AAFdYngZnb1IykyHAHSVc28I7Slbm3Ee9Jg')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup =  types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://google.com'))
    markup.add(types.InlineKeyboardButton('Удалить фото', callback_date='delite'))
    markup.add(types.InlineKeyboardButton('Изменить текст', callback_date='edit'))
    bot.reply_to(message, 'Классное фото', reply_markup=markup)

@bot.message_handler(commands=['start','hello','good'])
def main(messege):
    bot.send_message(messege.chat.id,f'Привет , {messege.from_user.first_name} {messege.from_user.last_name}')

@bot.message_handler(commands=['help'])
def main(messege):
    bot.send_message(messege.chat.id,'<b>help: information</b>',parse_mode='html')

@bot.message_handler(commands=['info'])
def main(messege):
    bot.send_message(messege.chat.id, messege)

@bot.message_handler()
def info(messege):
    if messege.text.lower()== 'привет':
        bot.send_message(messege.chat.id, f'Привет , {messege.from_user.first_name} ' )
    elif messege.text.lower()=='id':
        bot.reply_to(messege , f'ID: {messege.from_user.id}')



bot.polling(none_stop=True)