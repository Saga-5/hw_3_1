from aiogram import types, Dispatcher
import random
from config import bot


async def echo(message: types.Message):
    if "game" in message.text.lower():
        games = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']
        game = random.choice(games)
        await bot.send_dice(chat_id=message.chat.id, emoji=game)
    else:
        await message.answer(message.text)


def register_commands_handlers(dp: Dispatcher):
    dp.register_message_handler(echo)
