from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

Admins = [1175324585, ]

token = config('BOT_TOKEN')
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)