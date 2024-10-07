from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot


async def quiz_1(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button = InlineKeyboardButton('Далее', callback_data='quiz_2')

    keyboard.add(button)

    question = 'BMW or Mercedes or Audi'

    answer = ['BMW', 'Mercedes', 'Audi']

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='BMW is better!',
        open_period=30,
        reply_markup=keyboard
    )

async def quiz_2(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button = InlineKeyboardButton('Далее', callback_data='quiz_3')

    keyboard.add(button)

    question = 'Сколько хромосом у человека?'

    answer = ['52', '67', '46', '16']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Ну ну)',
        open_period=30,
        reply_markup=keyboard
    )

async def quiz_3(call: types.CallbackQuery):
    question = 'Messi or Ronaldo'
    answer = ['Messi', 'Ronaldo', 'another', 'me']
    await bot.send_photo(chat_id=call.from_user.id,
                         photo=open('images/goats.jfif', 'rb'))

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation='Siuuu',
        open_period=30
    )


def register_handlers_quiz(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['q'])
    dp.register_callback_query_handler(quiz_2, text='quiz_2')
    dp.register_callback_query_handler(quiz_3, text='quiz_3')