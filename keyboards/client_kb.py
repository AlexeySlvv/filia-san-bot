from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b_help = KeyboardButton('/help')
b_from = KeyboardButton('/from_lang')
b_to = KeyboardButton('/to_lang')

kb_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_markup.row(b_from, b_to).add(b_help)
