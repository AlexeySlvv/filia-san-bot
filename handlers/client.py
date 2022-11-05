from aiogram import types
from aiogram import Dispatcher

from create_bot import dp

from googletran_help import gt_translate
from libretran_help import lt_translate


# @dp.message_handler(commands=['start', 'help'])
async def do_start_help(msg: types.Message):
    await msg.answer('Multi-service text translation. Please, send me your text to translate')


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
    dp.register_message_handler(do_start_help, commands=['start', 'help'])
    dp.register_message_handler(do_reply)
