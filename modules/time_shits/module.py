import requests
from random import choice
from bs4 import BeautifulSoup
from modules.base_module import BaseModule


class TS(BaseModule):

    @staticmethod
    def get_random_TS():

        timeShits = ['Скайп с Демидовым Д. Обзор выполнения карьерного плана на испытательный срок', 'Подготовка отчета по всем задачам испытательного срока','Разворачивание MVP на новой виртуальной машине']
        TS = []
        for timeShit in timeShits:
            text = timeShit.text.strip()
            TSs.append({'text':text})
        return (choice(TSs))

    def run(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Generation TS"
        try:
            TS = TS.get_random_TS()
            message_text = '\n{0}\n<a href="{1}"><i>TS </i></a>'.format(TS['text'])
        except:
            self.send(update, context, text="Что-то пошло не так")


random_TS_module = RandomTS()
