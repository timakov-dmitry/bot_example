from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from imageai.Detection import ObjectDetection
threshold = 70
import os

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolo.h5")
detector.loadModel()


updater = Updater(token='1685734491:AAEMp2ZOAy6Hya0U9LKF28IhLQzhomNcXDA', use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Я могу находить объекты на изображениях")


def set_threshold_handler(update, context):
    threshold = 40
    context.bot.send_message(chat_id=update.effective_chat.id, text="Установила")


def on_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Пришли картинку!")


def on_image(update, context):
    file = context.bot.getFile(update.message.photo[1].file_id)
    file.download('image.jpg')
    detections = detector.detectObjectsFromImage(input_image="image.jpg",
                                                 output_image_path="image_result.jpg",
                                                 minimum_percentage_probability=threshold)
    text = ', '.join([image_object["name"] for image_object in detections])
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('image_result.jpg', 'rb'))


start_handler = CommandHandler('start', start)
set_threshold_handler = CommandHandler('set_threshold', set_threshold_handler)
message_handler = MessageHandler(Filters.text & (~Filters.command), on_message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(MessageHandler(Filters.photo, on_image))

print('Bot started...')
updater.start_polling()
