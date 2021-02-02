from random import randrange, choice


def generate_password(update, context):
    symbols='1234567890-=qwertyuiopasdfghjklzxcvbnm,./!^&*()_+QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?`~[]'
    l = randrange(8,16)
    password_ = ""
    for t in range(l):
        password_+= choice(symbols)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Это твой пароль: "+password_+"\nНикому не сообщай его!")