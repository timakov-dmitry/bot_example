from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from modules.password_generator.module import generate_password
from modules.image_classificator.module import on_image, set_threshold_handler


updater = Updater(token='1685734491:AAEMp2ZOAy6Hya0U9LKF28IhLQzhomNcXDA', use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Я могу находить объекты на изображениях")


def on_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Пришли картинку!")


start_handler = CommandHandler('start', start)
generate_password_handler = MessageHandler(Filters.text(['Пароль','пароль','password']), generate_password)
set_threshold_handler = CommandHandler('set_threshold', set_threshold_handler)
message_handler = MessageHandler(Filters.text & (~Filters.command), on_message)

dispatcher.add_handler(generate_password_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(MessageHandler(Filters.photo, on_image))

print('Bot started...')
updater.start_polling()
