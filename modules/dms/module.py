# -*- coding: utf8 -*-

from modules.base_module import BaseModule
import telegram

class dms(BaseModule):
    def run(self, update, context):

        keyboard = telegram.ReplyKeyboardMarkup([['Организовать мед. помощь!'], ['Памятка по ДМС'], ['Телемедицина'], ['Куда написать с любыми вопросами по ДМС?'], ['Приложение АльфаСтрахование']], one_time_keyboard=True)
        msg = update.message.text

        if msg == 'дмс':
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Для получения информации воспользуйтесь подсказками ниже',
                                     reply_markup=keyboard)

        elif msg == 'Организовать мед. помощь!':
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Служба организации медицинской помощи АО «АльфаСтрахование» 8-800-700-09-98. Необходимо сообщить диспетчеру АО «АльфаСтрахование» номер страхового полиса (имеется на полисе) или ФИО застрахованного, точный адрес места происшествия, характер происшествия и ожидать бригады, при ухудшении связаться с диспетчерской.',
                                     reply_markup=keyboard)

        elif msg == 'Телемедицина':
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Телемедицинские услуги Доктор рядом онлайн осуществляются на сайте https://telemed.drclinics.ru/, необходимо зарегистрироваться в личном кабинете, указать номер полиса, фамилию, имя и отчество, дату рождения, номер мобильного телефона, или в мобильном приложении «АльфаСтрахование Мобайл». Телемедицинские консультации врача-терапевта, узких специалистов по предварительной записи по расписанию врача.',
                                     reply_markup=keyboard)

        elif msg == 'Памятка по ДМС':
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Скачать памятку: https://my.lanit.ru/news/Documents/pamyatka2021.docx (необходимо осуществить вход на корпоративный портал Норбит)',
                                     reply_markup=keyboard)

        elif msg == 'Куда написать с любыми вопросами по ДМС?':
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Выделенный почтовый ящик для обращений сотрудников ГК ЛАНИТ в АО «АльфаСтрахование» Lanit@alfastrah.ru',
                                     reply_markup=keyboard)

        elif msg == 'Приложение АльфаСтрахование':
             context.bot.send_message(chat_id=update.effective_chat.id,
                                      text='Мобильное приложение «АльфаСтрахование Мобайл»- это ваш верный помощник в чрезвычайной ситуации и надёжный хранитель знаний обо всех страховых полисах - https://mobile.alfastrah.ru/ (требуется регистрация).',
                                      reply_markup=keyboard)

dms_module = dms()