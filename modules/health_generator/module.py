from modules.base_module import BaseModule
from random import randint
import requests
from bs4 import BeautifulSoup

class GenerateHealth(BaseModule):
    def run(self, update, context):
        r1 = requests.get('https://dartoffice.ru/blog/19_zdorove-v-ofise-7-poleznykh-sovetov.html')
        html_rus = BeautifulSoup(r1.content, features=("lxml"))

        advise = html_rus.find("div", {"class":"blog_content mar_b2"})
        advise_title = advise.find_all("h2")

        data = []
        for h2 in advise.find_all("h2"):
            data.append([strong.get_text().split('+')[0] for strong in h2.find_all("strong")])
        del data[0]


        data_body = []
        advise_body = advise.find_all("span", {'style': 'font-size: 14pt;'})


        data_full = []
        number_of_paragraf = [7,8,11,12,15,16,19,20,23,24,25,26,27,28,31,32,36,38]
        for i in number_of_paragraf:
            data_full.append(advise_body[i].text)
        data_new_new = data_full

        data_new_new[0] = data_new_new[0]  + data_new_new[1]
        del data_new_new[1]

        data_new_new[1] = data_new_new[1]  + data_new_new[2]
        del data_new_new[2]

        data_new_new[2] = data_new_new[2]  + data_new_new[3]
        del data_new_new[3]

        data_new_new[3] = data_new_new[3]  + data_new_new[4]
        del data_new_new[4]

        data_new_new[4] = data_new_new[4] + data_new_new[5]
        del data_new_new[5]

        data_new_new[4] = data_new_new[4] + data_new_new[5]
        del data_new_new[5]

        data_new_new[4] = data_new_new[4] + data_new_new[5]
        del data_new_new[5]

        data_new_new[4] = data_new_new[4] + data_new_new[5]
        del data_new_new[5]

        data_new_new[4] = data_new_new[4] + data_new_new[5]
        del data_new_new[5]

        data_new_new[5] = data_new_new[5] + data_new_new[6]
        del data_new_new[6]

        data_new_new[6] = data_new_new[6] + data_new_new[7]
        del data_new_new[7]

        rand = randint(0, 7)

        final_advice = "{0} \n {1}".format(*data[rand], data_new_new[rand])
        self.send(update, context, final_advice)

generate_health_module = GenerateHealth()