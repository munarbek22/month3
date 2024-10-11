from aiogram import  executor
import logging
from config import dp, bot
from handlers import commands, echo, quiz, game, FSM_reg

# FSM_reg.register_handlers_registration(dp)
FSM_reg.register_handlers_store(dp)
game.register_game(dp)
commands.register_handlers_commands(dp)
quiz.register_handlers_quiz(dp)

echo.register_handlers_echo(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
