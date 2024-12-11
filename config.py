from aiogram import Bot , Dispatcher
from decouple import config

token = config('TOKEN')

Admins = [1882414934, ]

bot = Bot(token = token)
dp = Dispatcher(bot)