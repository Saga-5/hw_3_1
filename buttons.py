from turtledemo.penrose import start

from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

cansel_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
censel_button = KeyboardButton(text="Отмена!!!")
cansel_markup.add(censel_button)

