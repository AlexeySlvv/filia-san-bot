from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lang_dict import LANG_DICT

kb_lang = ReplyKeyboardMarkup(resize_keyboard=True)

# for lang in LANG_DICT:
#     kb_lang.add(KeyboardButton(lang))

kb_lang.row(*[KeyboardButton(lang) for lang in LANG_DICT])

# kb_lang.add('Отмена')
