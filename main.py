import telebot

TOKEN = '1413563921:AAGrnWRrtEaf3i10EVTi2VPbcAc2gu4qaKo'

bot = telebot.TeleBot(TOKEN)
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    text = ''.join(message.text.split()).lower()
    if text == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAM0X-CLzma41DmZslBUQ3BhaBYB8ncAAo4AAxZCawq-pIZ9bX4tXB4E')
    elif text == 'пока':
        bot.send_message(message.chat.id, f'Прощай, {message.from_user.first_name}')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAM6X-CMNb0Z6bFqu4iZgPgr1FPDQQMAAmADAAK1cdoGOMP4Rre0H5weBA')
    elif text == 'ятебялюблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif text == "как дела?":
        bot.send_message(message.chat.id, 'Хорошо, а у тебя?')
    else:
        bot.send_message(message.chat.id, 'Простите, я вас не понял :(')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()
