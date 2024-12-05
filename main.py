from aiogram import types , executor
from Home_work1 import bot , dp
import logging
import os

@dp.message_handler(commands=["start", "help"])
async def start_handler(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=(
            f"id {message.from_user.id}!\n"
            f"Пожалуйста, ваш id — {message.from_user.id}"
        )
    )



@dp.message_handler(commands=["music"])
async def music_handler(message: types.Message):
    photo_path = os.path.join('media', 'img.png')
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo=photo, caption="Советую послушать !!!")


#---------------------------------------------------------------------------------------------------------
@dp.message_handler()
async def echo_handler(message: types.Message):
    try:
        number = float(message.text)
        await message.answer(f'Ваше число в квадрате {number ** 2}')
    except ValueError:
        await message.answer(message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp , skip_updates=True)
