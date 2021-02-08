import requests
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, Filters
from modules.base_module import BaseModule


class Weather(BaseModule):

    def weather_parser(self, s_city):
        appid = '11c0d3dc6093f7442898ee49d2430d20'
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        if len(data['list']) > 0:
            city_id = data['list'][0]['id']

            res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                               params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()
            temp = data['main']['temp']
            result = f'Температура в городе {s_city} : {temp} °С'
        else:
            result = "Город не найден. Введите команду \"Погода\" заново"
        return result

    def stop(self, update, context):
        self.send(update, context, text='Жаль. Было бы интересно пообщаться. Хорошего дня!')
        return ConversationHandler.END

    def get_handler(self, query):
        return ConversationHandler(
            entry_points=[MessageHandler(Filters.text(query), tmp)],
            states={
                0: [MessageHandler(Filters.text, tmp)],
                1: [MessageHandler(Filters.text, tmp1)],

            },
            fallbacks=[MessageHandler(Filters.text(['Закончить', 'закончить']), self.stop)]
        )


def tmp(update, context):
    weather_module.send(update, context, text='Температуру какого города вы хотите узнать?')
    return 1


def tmp1(update, context):
    city = update.message.text
    result = weather_module.weather_parser(city)
    weather_module.send(update, context, text=result)
    return ConversationHandler.END


weather_module = Weather()
