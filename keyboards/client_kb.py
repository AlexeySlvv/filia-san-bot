from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b_start = KeyboardButton('/start')
b_settings = KeyboardButton('/settings')
b_help = KeyboardButton('/help')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.row(b_start, b_settings, b_help)
