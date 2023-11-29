import telebot
bot = telebot.TeleBot('6757234753:AAGUi0Hn_3qAuA_tpzxMwLGSZcq7v6NFdXg')

@bot.message_handler(commands=['start'])
def maincommand(message):
    bot.send_message(message.chat.id, 'Привет! Я Анекдотер.\nВсё, что я умею - присылать анекдоты. Чтобы получить анекдот, напишите число от 1 до 5')


@bot.message_handler(commands=['1'])
def command1(message):
    bot.send_message(message.chat.id, 'Штирлиц всю ночь топил камин. На утро камин утонул.')


@bot.message_handler(commands=['2'])
def command2(message):
    bot.send_message(message.chat.id, 'Письмо из центра до Штиpлица не дошло... Пришлось читать во второй раз.')


@bot.message_handler(commands=['3'])
def command3(message):
    bot.send_message(message.chat.id, 'Штирлицу за шиворот упала гусеница. "Где-то взорвался танк," -- подумал Штирлиц.')


@bot.message_handler(commands=['4'])
def command4(message):
    bot.send_message(message.chat.id, 'Уважаемый Артём Фролов! С вашего счёта списано $500.')


@bot.message_handler(commands=['5'])
def command5(message):
    bot.send_message(message.chat.id, 'Штирлиц шёл в Дрезден с трудом разбирая дорогу.\nНаутро железная дорога от Берлина до Дрездена была полностью разобрана...')


bot.infinity_polling()
