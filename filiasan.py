from translatepy.translators.google import GoogleTranslate
from libretran_help import lt_translate

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import argparse

parser = argparse.ArgumentParser(description='Filisia telegram bot')
parser.add_argument('-t', '--token', help='Filisia token file')

# token
try:
    args = parser.parse_args()
    with open(args.token, 'r') as t_f:
        TOKEN = t_f.read()
        bot = Bot(token=TOKEN)
        dp = Dispatcher(bot)
except Exception as e:
    print('Token file error:', str(e))
    exit()


gtranslate = GoogleTranslate()


@dp.message_handler()
async def do_reply(msg: types.Message):
    # TODO from-to languages

    lt_text = f"Libre translate:\n{lt_translate(msg.text, lang_to='ru')}"
    await msg.reply(lt_text)

    gt_text = f"Google translate:\n{gtranslate.translate(msg.text, 'Russian')}"
    await msg.reply(gt_text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
