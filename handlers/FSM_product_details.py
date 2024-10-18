from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons
from db import db_main

class fsm_product_details(StatesGroup):
    category = State()
    info_product = State()
    product_id = State()
    create = State()

async def start_details(message: types.Message):
    await message.answer('Введите категорию товара: ')
    await fsm_product_details.category.set()
async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text
    await message.answer('Введите информацию о товаре: ')
    await fsm_product_details.next()
async def load_info_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info_product'] = message.text
    await message.answer('Введите ID товара: ')
    await fsm_product_details.next()
async def load_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info_product'] = message.text

async def create(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await db_main.sql_insert_product_details(
            category=data['category'],
            info_product=data['info_product'],
            product_id=data['product_id'],
        )

def register_handlers_details(dp: Dispatcher):
    dp.register_message_handler(start_details, commands=['prod'])
    dp.register_message_handler(load_category, state=fsm_product_details.category)
    dp.register_message_handler(load_info_product, state=fsm_product_details.info_product)
    dp.register_message_handler(load_product_id, state=fsm_product_details.product_id)
    dp.register_message_handler(create, state=fsm_product_details.create)

