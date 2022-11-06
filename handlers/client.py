from aiogram import types
from aiogram import Dispatcher

from create_bot import dp

from googletran_help import gt_translate
from libretran_help import lt_translate

from keyboards import kb_markup

# @dp.message_handler(commands=['start'])
async def do_start(msg: types.Message):
    await msg.answer('Multi-service text translation. Please, send me your text to translate', reply_markup=kb_markup)


async def do_help(msg: types.Message):
    await msg.answer('Multi-service text translation. Please, send me your text to translate')


async def do_from_lang(msg: types.Message):
    await msg.answer('From language')


async def do_to_lang(msg: types.Message):
    await msg.answer('To language')


# @dp.message_handler()
async def do_reply(msg: types.Message):
    # TODO from-to languages
    # TODO service to the end

    lt_text = lt_translate(msg.text, lang_to='ru')
    if lt_text:
        lt_text += '\n\nLibreTranslate libretranslate.com'
        await msg.reply(lt_text)

    gt_text = gt_translate(msg.text, lang_to='Russian')
    if gt_text:
        gt_text += "\n\nGoogle Translate translate.google.com"
        await msg.reply(gt_text)


def register_client_handlers():
    dp.register_message_handler(do_start, commands=['start'])
    dp.register_message_handler(do_help, commands=['help'])
    dp.register_message_handler(do_from_lang, commands=['from_lang'])
    dp.register_message_handler(do_to_lang, commands=['to_lang'])
    dp.register_message_handler(do_reply)
