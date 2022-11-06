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
По умолчанию язык определяется автоматически и переводится на русский.
Для настройки перевода нажмите или отпарвьте команду "/settings".''')


# @dp.message_handler()
async def do_reply(msg: types.Message):
    lt_text = lt(
        msg.text, lang_from=LANG_DICT[settings.lang_from][1], lang_to=LANG_DICT[settings.lang_to][1])
    if lt_text:
        lt_text += '\n\nLibreTranslate libretranslate.com'
        await msg.reply(lt_text)

    gt_text = gt(
        msg.text, lang_from=LANG_DICT[settings.lang_from][0], lang_to=LANG_DICT[settings.lang_to][0])
    if gt_text:
        gt_text += "\n\nGoogle Translate translate.google.com"
        await msg.reply(gt_text)


def register_client_handlers():
    dp.register_message_handler(do_start, commands=['start'])
    dp.register_message_handler(do_help, commands=['help'])
    dp.register_message_handler(do_reply)
