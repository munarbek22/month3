from aiogram import executor
import logging
from config import dp, bot, Admins
from handlers import commands, echo, quiz, FSM_reg, FSM_store, send_products, send_and_delete_produucts
from db import db_main
from handlers.send_products import sendall_products


async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin,
                               text='Бот включен!')
        await db_main.sql_create()


commands.register_handlers_commands(dp)
quiz.register_handlers_quiz(dp)
FSM_reg.register_handlers_registration(dp)
FSM_store.register_handlers_store(dp)

send_products.register_send_handler(dp)
send_and_delete_produucts.register_send_handler(dp)

echo.register_handlers_echo(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup,
                           allowed_updates=['callback'])