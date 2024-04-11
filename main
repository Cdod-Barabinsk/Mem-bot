import random
import telebot
from telebot import types
import os
import glob

bot = telebot.TeleBot("Token")

# Путь к папке с картинками
image_folder_path = 'mems'

# Получить список файлов с расширением .jpg в папке
image_files = glob.glob(os.path.join(image_folder_path, '*.jpeg'))

sent_images = []

@bot.message_handler(commands=["start"])

def handle_start(message):
    keyboard = types.ReplyKeyboardMarkup(True)
    button1 = types.KeyboardButton("mem")
    keyboard.add(button1)
    bot.send_message(message.chat.id, "Привет, я мем-бот. Для получения мема нажми кнопку 'mem'", reply_markup=keyboard)
@bot.message_handler(func=lambda message: message.text == "mem")


def handle_mem(message):
    send_random_image(message.chat.id)


def send_random_image(chat_id):
    # Получить список изображений, которые еще не были отправлены
    available_images = [image for image in image_files if image not in sent_images]
    if not available_images:
        bot.send_message(chat_id, "Все мемы уже отправлены! Дождитесь поплнения базы мемов")
        return
    random_image = random.choice(available_images)
    sent_images.append(random_image)  # Добавить отправленное изображение в список
    with open(random_image, 'rb') as photo:
        bot.send_photo(chat_id, photo)

bot.polling(none_stop=True)
