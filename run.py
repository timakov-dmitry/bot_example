from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from modules.password_generator.module import generate_password
from modules.image_classificator.module import on_image, set_threshold_handler
from modules.advice_generator.module import generate_advice
from modules.what_eat.module import chose_food


updater = Updater(token='1685734491:AAEMp2ZOAy6Hya0U9LKF28IhLQzhomNcXDA', use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Я могу находить объекты на изображениях")


def on_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Пришли картинку!")


start_handler = CommandHandler('start', start)
generate_password_handler = MessageHandler(Filters.text(['Пароль','пароль','password']), generate_password)
advice_generator_handler = MessageHandler(Filters.text(['Дай совет','Что посоветуешь','совет']), generate_advice)

set_threshold_handler = CommandHandler('set_threshold', set_threshold_handler)
message_handler = MessageHandler(Filters.text & (~Filters.command), on_message)
what_eat_handler = MessageHandler(Filters.text(['Что поесть',"Что выбрать поесть","еда","есть","поесть","что выбрать"]), chose_food)
dispatcher.add_handler(what_eat_handler)
dispatcher.add_handler(generate_password_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(advice_generator_handler)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(MessageHandler(Filters.photo, on_image))

print('Bot started...')
updater.start_polling()
