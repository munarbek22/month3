from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# =============================
# cancel = ReplyKeyboardMarkup(resize_keyboard=True)
#
# cancel_button = KeyboardButton('Отмена')
# cancel.add(cancel_button)
# =============================
cancel = ReplyKeyboardMarkup(resize_keyboard=True).add (KeyboardButton('Отмена'))
# ========================================
# cancel = ReplyKeyboardMarkup(resize_keyboard=True)
# cancel.add(KeyboardButton('Отмена'))




size_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
size_keyboard.add(KeyboardButton('XS'))
size_keyboard.add(KeyboardButton('S'))
size_keyboard.add(KeyboardButton('M'))
size_keyboard.add(KeyboardButton('L'))
size_keyboard.add(KeyboardButton('XL'))
size_keyboard.add(KeyboardButton('2XL'))
size_keyboard.add(KeyboardButton('3XL'))
