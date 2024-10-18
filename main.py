from aiogram import  executor
import logging
from config import dp, bot, Admins
from handlers import commands, echo, quiz, game, FSM_reg, FSM_store, FSM_product_details
from handlers.commands import send_picture_handler
from db import db_main, queries

async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin,
                               text='Бот включен!')

async def on_shutdown(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin,
                               text='я пошел спать')

        await db_main.sql_create()


FSM_product_details.register_handlers_details(dp)
FSM_store.register_handlers_store(dp)
# FSM_reg.register_handlers_registration(dp)
FSM_reg.register_handlers_store(dp)
game.register_game(dp)
commands.register_handlers_commands(dp)
quiz.register_handlers_quiz(dp)

echo.register_handlers_echo(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
