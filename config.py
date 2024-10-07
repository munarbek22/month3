from aiogram import Bot, Dispatcher
from decouple import config

token = config('BOT_TOKEN')
bot = Bot(token=token)
dp = Dispatcher(bot)