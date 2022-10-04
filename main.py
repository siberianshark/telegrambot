import telebot
from telebot import types
bot = telebot.TeleBot('5607010905:AAElKe4G5bKaAgaJHBpf7DVTsU2bXi5TAF0')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, <b>{message.from_user.fist_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

#@bot.message_handler(content_types=['text'])
#def get_user_text(message):
#    if message.text == "Hello":
#       bot.send_message(message.chat.id, "Hello!", parse_mode='html')
#   elif message.text == "id":
#       bot.send_message(message.chat.id, f" Your ID: {message.from_user.id}", parse_mode='html')
#   elif message.text == "photo":
#       photo = open('shark-animals-gray-wallpaper.jpg', 'rb')
#      bot.send_photo(message.chat.id, photo)
#  else:
#     bot.send_message(message.chat.id, f" I do not understand ", parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Great pic!')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Visit our website", url="https://a-z-animals.com/animals/shark/"))
    bot.send_message(message.chat.id, 'Follow to our website', reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('Website')
    start = types.KeyboardButton('Start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Hahahahha', reply_markup=markup)


bot.polling(none_stop=True)
