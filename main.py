import telebot as tb
import sqlite3 as sq


bot = tb.TeleBot("6342056304:AAFLOpRAd4Be5ZEkatMP7NAV0WbzNz-kvBA")

@bot.message_handler(commands=['start'])
def main(message: tb.types.Message):
    connection = sq.connect('DataBase.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (user TEXT UNIQUE, scores INTEGER)""")
    cursor.execute("INSERT OR IGNORE INTO users VALUES (?, ?)", (message.from_user.username, 1))
    connection.commit()
    cursor.close()
    connection.close()
    if message:
        bot.send_message(message.chat.id, "Hello there!")
        bot.send_message(message.chat.id, "Hello there!")

@bot.message_handler(content_types=['audio', 'voice'])
def main(message):
    if message:
        bot.send_message(message.chat.id, "🗿🗿")

@bot.message_handler(content_types=['sticker'])
def main(message):
    if message:
        bot.send_message(message.chat.id, "I know that it's a sticker!")

@bot.message_handler(commands=['menu'])
def main(message):
    menu = tb.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)
    button1 = tb.types.KeyboardButton('Give phone number', request_contact=True)
    button2 = tb.types.KeyboardButton("Press 'F' to pay respect")
    button3 = tb.types.KeyboardButton('Give location', request_location=True)
    button4 = tb.types.KeyboardButton('Setup a quiz', request_poll=tb.types.KeyboardButtonPollType())
    menu.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, "🗿", reply_markup=menu)

@bot.message_handler(commands=['menu2'])
def main(message):
    menu = tb.types.InlineKeyboardMarkup(row_width=2)
    button1 = tb.types.InlineKeyboardButton(text='Hey! this is a text lol', callback_data='str')
    button2 = tb.types.InlineKeyboardButton(text='Hello World', url='https://youtu.be/dQw4w9WgXcQ?si=6arKtjHbC2DMmw4h')
    button3 = tb.types.InlineKeyboardButton(text='None', url='https://youtu.be/dQw4w9WgXcQ?si=6arKtjHbC2DMmw4h')
    button4 = tb.types.InlineKeyboardButton(text='4th button', callback_data='🗿')
    menu.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, 'menu?', reply_markup=menu)

@bot.callback_query_handler(func=lambda call:call.data=='str')
def main(call):
    bot.send_message(call.message.chat.id, 'text lol')

@bot.callback_query_handler(func=lambda call:call.data=='🗿')
def main(call):
    bot.send_message(call.message.chat.id, call.data)

@bot.message_handler(content_types=['text'])
def main(message: tb.types.Message):
    if message.text == 'Give phone number':
        bot.send_message(message.chat.id, "")
    elif message.text == "Press 'F' to pay respect":
        bot.send_message(message.chat.id, "F")
    elif message.text == 'Give location':
        bot.send_message(message.chat.id, "")
    elif message.text == 'Setup a quiz':
        bot.send_message(message.chat.id, "")

@bot.message_handler(content_types=['contact'])
def main(message: tb.types.Message):
    phone_numbers = open('Phone_Numbers.txt', mode='r').readlines()
    with open('Phone_Numbers.txt', mode='a') as file:
        if message.contact.phone_number not in phone_numbers:
            file.write(message.contact.phone_number + '\n')

@bot.message_handler(content_types=['location'])
def main(message: tb.types.Message):
    locations = open('Locations.txt', mode='r').readlines()
    with open('Locations.txt', mode='a') as file:
        if f'{message.location.longitude} {message.location.latitude}\n' not in locations:
            file.write(f'{message.location.longitude} {message.location.latitude}\n')
bot.polling(non_stop=True)