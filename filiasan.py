from collections import defaultdict
from typing import OrderedDict

import argparse

import nest_asyncio

from telegram import Update
from telegram.ext import filters, ApplicationBuilder, MessageHandler

import nltk
from nltk.corpus import wordnet as wn

from translatepy.translators.google import GoogleTranslate
from libretran_help import lt_translate

parser = argparse.ArgumentParser(description='Filia-san telegram bot')
parser.add_argument('-f', '--token', help='bot token file')


# token
try:
    args = parser.parse_args()
    with open(args.token, 'r') as t_f:
        TOKEN = t_f.read()
except Exception as e:
    print('Token file error:', str(e))
    exit()


nltk.download('wordnet')
nltk.download('omw-1.4')


POS_DICT = OrderedDict({
    'n': 'Noun',
    'v': 'Verb',
    'a': 'Adjective',
    's': 'Adjective sattelite',
    'r': 'Adverb',
})


nest_asyncio.apply()


gtranslate = GoogleTranslate()


def bot_do(text: str) -> str:
    bot_text = str()

    # TODO from-to languages
    # bot_text += f"{gtranslate.translate(text, 'Russian')}"
    bot_text += f"{lt_translate(text, lang_to='ru')}"

    # WordNet
    synsets = wn.synsets(text)
    if synsets:
        syn_dict = defaultdict(list)
        for syn in synsets:
            syn_dict[syn.pos()].append(syn.definition())

        for pos in POS_DICT:
            definitions = syn_dict.get(pos)
            if definitions:
                bot_text += f"\n\n{POS_DICT[pos]}\n"
                for definition in definitions:
                    bot_text += f'\n * {definition}\n'
                bot_text += '\n'

    return bot_text if bot_text else 'Sorry, nothing was found'


async def reply(update: Update, context) -> None:
    user_text = update.message.text.lower()
    bot_reply = bot_do(user_text)
    await update.message.reply_text(bot_reply)


if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    handler = MessageHandler(filters.Text(), reply)
    app.add_handler(handler)
    app.run_polling()
