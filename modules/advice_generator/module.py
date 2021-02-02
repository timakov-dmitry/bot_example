import requests
from bs4 import BeautifulSoup

def generate_advice(update, context):
    resp = requests.get(url='http://old.randomes.top/sovet.php', headers=[])
    advice = (BeautifulSoup(resp.text).
                find('div', {'id': 'main'}).
                find('span').
                text)

    context.bot.send_message(chat_id=update.effective_chat.id, text="🔮 "+advice)
