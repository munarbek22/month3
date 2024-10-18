from Tools.scripts.generate_opcode_h import internal_footer
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons
from db import db_main
class fsm_store(StatesGroup):
    name_product = State()
    size = State()
    category = State()
    price = State()
    photo = State()
    submit = State()

async def start_store(message: types.Message):
    await message.answer('Введите название товара: ')
    await fsm_store.name_product.set()
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_product'] = message.text
    await message.answer('Введите размер товара: ')
    await fsm_store.next()
async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text
    await message.answer('Введите категорию товара: ')
    await fsm_store.next()
async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text
    await message.answer('Введите цену товара: ')
    await fsm_store.next()
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await message.answer('Отправьте фото товара: ')
    await fsm_store.next()
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
    await message.answer_photo(photo=data['photo'], caption=f'Верные ли данные: \n'
                                                              f'Название - {data["name_product"]}\n'
                                                              f'Размер - {data["size"]}\n'
                                                              f'Категория - {data["category"]}\n'
                                                              f'Цена - {data["price"]}\n', reply_markup=buttons.submit)
    await fsm_store.next()
async def submit(message: types.Message, state: FSMContext):
    if message.text == 'Да':
        async with state.proxy() as data:
            await db_main.sql_insert_store(
                name_product=data['name_product'],
                size=data['size'],
                price=data['price'],
                photo=data['photo']
            )
        await message.answer('Товар в базе!')
        await state.finish()
    elif message.text == 'Нет':
        await message.answer('Отменено!')
        await state.finish()
    else:
        await message.answer('Для дальнейщего действия, нажмите на кнопки ниже')
async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    kb = types.ReplyKeyboardRemove()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=kb)
def register_handlers_store(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm,
                                Text(equals='Отмена',
                                     ignore_case=True),
                                    state='*')
    dp.register_message_handler(start_store, commands=['store'])
    dp.register_message_handler(load_name, state=fsm_store.name_product)
    dp.register_message_handler(load_size, state=fsm_store.size)
    dp.register_message_handler(load_category, state=fsm_store.category)
    dp.register_message_handler(load_price, state=fsm_store.price)
    dp.register_message_handler(load_photo, state=fsm_store.photo, content_types=['photo'])
    dp.register_message_handler(submit, state=fsm_store.submit)



