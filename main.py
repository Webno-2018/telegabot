import telebot

from extensions import APIException, CryptoConverter

from extensions import keys, TOKEN
#ConvertionException


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
    text = ('Чтобы бот начал работу введите команду в следующем формате: \n<имя валюты>'
            '\n<в какую валюту перевести>'
            '\n<сумма переводимой валюты>\n'
            '\nВы можете увидеть список всех доступных валют,'
            ' введя команду: /values')

    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def help(message: telebot.types.Message):
    text = "Доступные валюты:"

    for key in keys.keys():
        text = '\n'.join((text, key, ))

    bot.reply_to(message, text)


#convert
@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Слишком много параметров')

        base, quote, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)

    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n{e}')

    else:
        text = f'{amount} {quote} стоит {total_base} {base}'
        bot.send_message(message.chat.id, text)


bot.polling()
