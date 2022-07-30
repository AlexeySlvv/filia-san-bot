from collections import defaultdict
from typing import OrderedDict

import nest_asyncio

from telegram import Update
from telegram.ext import filters, ApplicationBuilder, MessageHandler

import nltk
from nltk.corpus import wordnet as wn
from pystardict import Dictionary

try:
    with open('../.tokens/filiasan_bot', 'r') as t_f:
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


dict_en_ru = Dictionary('./dict/korolew/dictd_www.mova.org_korolew_enru')
dict_ru_en = Dictionary('./dict/korolew/dictd_www.mova.org_korolew_ruen')


nest_asyncio.apply()


def bot_do(text: str) -> str:
    bot_text = str()

    # En-Ru
    tran = dict_en_ru.get(text)
    if tran:
        bot_text += tran+'\n'

    # WordNet
    synsets = wn.synsets(text)
    if synsets:
        syn_dict = defaultdict(list)
        for syn in synsets:
            syn_dict[syn.pos()].append(syn.definition())

        for pos in POS_DICT:
            definitions = syn_dict.get(pos)
            if definitions:
                bot_text += POS_DICT[pos]+'\n'
                for definition in definitions:
                    bot_text += f'\n * {definition}\n'
                bot_text += '\n'

    # Ru-En
    tran = dict_ru_en.get(text)
    if tran:
        bot_text += tran+'\n'

    return bot_text if bot_text else 'Ничего не найдено'


async def reply(update: Update, context) -> None:
    user_text = update.message.text.lower()
    bot_reply = bot_do(user_text)
    await update.message.reply_text(bot_reply)


if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    handler = MessageHandler(filters.Text(), reply)
    app.add_handler(handler)
    app.run_polling()
