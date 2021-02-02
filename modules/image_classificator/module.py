from imageai.Detection import ObjectDetection

threshold = 70

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("modules/image_classificator/yolo.h5")
detector.loadModel()


def on_image(update, context):
    file = context.bot.getFile(update.message.photo[1].file_id)
    file.download('image.jpg')
    detections = detector.detectObjectsFromImage(input_image="image.jpg",
                                                 output_image_path="image_result.jpg",
                                                 minimum_percentage_probability=threshold)
    text = ', '.join([image_object["name"] for image_object in detections])
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('image_result.jpg', 'rb'))


def set_threshold_handler(update, context):
    threshold = 40
    context.bot.send_message(chat_id=update.effective_chat.id, text="Установила")