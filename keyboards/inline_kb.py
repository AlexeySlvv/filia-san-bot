from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb_googletran = InlineKeyboardMarkup()
kb_googletran.add(InlineKeyboardButton('Google Translate', url='https://translate.google.com'))
kb_libretran = InlineKeyboardMarkup()
kb_libretran.add(InlineKeyboardButton('LibreTranslate', url='https://libretranslate.com'))
