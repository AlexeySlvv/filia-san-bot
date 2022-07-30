from collections import defaultdict
from typing import OrderedDict

import nest_asyncio

from telegram import Update
from telegram.ext import filters, ApplicationBuilder, MessageHandler, ConversationHandler

import nltk
from nltk.corpus import wordnet as wn
from pystardict import Dictionary
import langid

try:
    with open('../.tokens/filiasan_bot', 'r') as t_f:
        TOKEN = t_f.read()
except:
    print('Token file error')
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
#dict_en_ru = Dictionary('./dict/wiktionary_en-ru_stardict_2022-07-20/Wiktionary English-Russian/Wiktionary English-Russian')
dict_es_ru = Dictionary('./dict/wiktionary_es-ru_stardict_2022-07-17/Wiktionary Spanish-Russian/Wiktionary Spanish-Russian')
dict_ru_en = Dictionary('./dict/korolew/dictd_www.mova.org_korolew_ruen')
dict_ru_es = Dictionary('./dict/wiktionary_ru-es_stardict_2022-07-07/Wiktionary Russian-Spanish/Wiktionary Russian-Spanish')


nest_asyncio.apply()


def bot_do(text: str) -> str:
    bot_text = str()
    #lang = langid.classify(text)[0]

    if True: #lang == 'en':
        # Перевод
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

    if True: #lang == 'es':
        tran = dict_es_ru.get(text)
        if tran:
            bot_text += tran+'\n'

    if True: #lang == 'ru':
        # Перевод
        tran = dict_ru_en.get(text)
        if tran:
            bot_text += tran+'\n'
        tran = dict_ru_es.get(text)
        if tran:
            bot_text += tran+'\n'

    #else:
        #bot_text = 'Я могу перевести слово только на русском или английском языке'

    return bot_text if bot_text else 'Ничего не найдено'


async def reply(update: Update, context) -> None:
    user_text = update.message.text.lower()
    bot_reply = bot_do(user_text)
    # print('<', user_text)
    # print('>', bot_reply)
    await update.message.reply_text(bot_reply)


if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    handler = MessageHandler(filters.Text(), reply)
    app.add_handler(handler)
    app.run_polling()

