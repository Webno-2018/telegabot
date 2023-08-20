import requests

import json

TOKEN = '6508767388:AAGlOzZjN9qFJ45IiwvYRe0eBUt2WrYS18Q'

keys = {
    'доллар':'USD',
    'евро':'EUR',
    'рубль':'RUB',
    'йена':'JPY',
    'юань':'CNY',
    'рупий':'INR',

}


#static method convert

class APIException(Exception):
    pass

class CryptoConverter():
    @staticmethod
    def convert(quote: str, base: str, amount: str):


        if base == quote:
            raise APIException(f'Нельзя конвертировать одинаковые валюты {base}')


        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать число {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать валюту {amount}')

        quote_ticker, base_ticker = keys[quote], keys[base]
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base