import config
import telebot



bot = telebot.TeleBot(config.TOKEN)

inst = False
other = False


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Instagram', 'Другое')
    bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
    global inst, other

    if message.text.lower() == 'instagram':
        bot.send_message(message.chat.id, 'Отправьте ссылку')
        inst = True
        other = False
    elif message.text.lower() == 'другое':
        bot.send_message(message.chat.id, 'Отправьте ссылку')
        other = True
        inst = False
    elif inst and message.text[-1] == '/':
        bot.send_message(message.chat.id, message.text + '?utm_source=instagram&utm_medium=direct')
        inst = False
    elif inst and message.text[-1] != '/':
        bot.send_message(message.chat.id, message.text + '/?utm_source=instagram&utm_medium=direct')
        inst = False
    elif other and message.text[-1] == '/':
        bot.send_message(message.chat.id, message.text + '?utm_source=messenger&utm_medium=other')
        other = False
    elif other and message.text[-1] != '/':
        bot.send_message(message.chat.id, message.text + '/?utm_source=messenger&utm_medium=other')
        other = False


bot.polling(none_stop=True)
