from aiogram import types

from create_bot import dp

from translaters.google_tran import translate as gt
from translaters.libre_tran import translate as lt

from keyboards import kb_client

from lang_dict import *

# @dp.message_handler(commands=['start'])


async def do_start(msg: types.Message):
    await msg.answer('Перевод текста с разных сервисов', reply_markup=kb_client)


async def do_help(msg: types.Message):
    await msg.answer('''Перевод текста с разных сервисов.
По умолчанию переводится с английского на русский.
Для настройки перевода нажмите или отпарвьте команду "/settings".''')


MARKUP_GT = types.InlineKeyboardMarkup()
MARKUP_GT.add(types.InlineKeyboardButton('Google Translate', 'https://translate.google.com'))
MARKUP_LT = types.InlineKeyboardMarkup()
MARKUP_LT.add(types.InlineKeyboardButton('LibreTranslate', 'https://libretranslate.com'))


# @dp.message_handler()
async def do_reply(msg: types.Message):
    gt_text = gt(
        msg.text, lang_from=LANG_DICT[settings.lang_from][0], lang_to=LANG_DICT[settings.lang_to][0])
    if gt_text:
        await msg.reply(gt_text, reply_markup=MARKUP_GT)

    lt_text = lt(
        msg.text, lang_from=LANG_DICT[settings.lang_from][1], lang_to=LANG_DICT[settings.lang_to][1])
    if lt_text:
        await msg.reply(lt_text, reply_markup=MARKUP_LT)


def register_client_handlers():
    dp.register_message_handler(do_start, commands=['start'])
    dp.register_message_handler(do_help, commands=['help'])
    dp.register_message_handler(do_reply)
