from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot



async def quiz_1(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton("Далее", callback_data="quiz_2")
    keyboard.add(button)

    question = 'XBOX or Sony?'
    answer = ['XBOX', 'Sony', 'Nintendo']

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Жаль...',
        open_period=60,
        reply_markup=keyboard
    )



async def quiz_2(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton("Далее", callback_data="quiz_3")
    keyboard.add(button)

    question = 'Python, Java, C++, C#, JavaScript?'
    answer = ['Python', 'Java', 'C++', 'C#', 'JavaScript']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='Все с тобой понятно -_-!',
        open_period=60,
        reply_markup=keyboard
    )


async def quiz_3(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton("Завершить", callback_data="end_quiz")
    keyboard.add(button)

    question = 'Что тяжелее: 1 кг ваты или 1 кг железа?'
    answer = ['1 кг ваты', '1 кг железа', 'Одинаково']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Одинаково, ведь это оба 1 кг!',
        open_period=60,
        reply_markup=keyboard
    )


async def end_quiz(call: types.CallbackQuery):
    await call.message.answer("Спасибо за участие в викторине! 🎉")


def register_quiz_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=["quiz"])
    dp.register_callback_query_handler(quiz_2, text="quiz_2")
    dp.register_callback_query_handler(quiz_3, text="quiz_3")
    dp.register_callback_query_handler(end_quiz, text="end_quiz")
