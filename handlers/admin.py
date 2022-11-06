from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.dispatcher.filters import Text

from create_bot import dp

from keyboards import kb_lang

from lang_dict import LANG_DICT

from translaters.google_tran import translate as gt
from translaters.libre_tran import translate as lt

class FSMAdmin(StatesGroup):
    lang_from = State()
    lang_to = State()
    translate = State()


# @dp.message_handler(commands=['settings'], state=None)
async def load_settings(msg: types.Message):
    await FSMAdmin.lang_from.set()
    await msg.reply('Язык текста', reply_markup=kb_lang)


# @dp.message_handler(state=FSMAdmin.lang_from)
async def load_from_lang(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['lang_from'] = msg.text
    await FSMAdmin.next()
    await msg.reply('Язык перевода')


# @dp.message_handler(state=FSMAdmin.lang_to)
async def load_to_lang(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['lang_to'] = msg.text
        await FSMAdmin.next()
        # TODO hide keyboard
        l1, l2 = data['lang_from'], data['lang_to']
        await msg.reply(f'Перевод с {l1} на {l2}. Введите текст')


async def do_translate(msg: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            l1, l2 = data['lang_from'], data['lang_to']
            lt_text = lt(msg.text, lang_from=LANG_DICT[l1][1], lang_to=LANG_DICT[l2][1])
            if lt_text:
                lt_text += '\n\nLibreTranslate libretranslate.com'
                await msg.reply(lt_text)

            gt_text = gt(msg.text, lang_from=LANG_DICT[l1][0], lang_to=LANG_DICT[l2][0])
            if gt_text:
                gt_text += "\n\nGoogle Translate translate.google.com"
                await msg.reply(gt_text)
    finally:
        await state.finish()


async def cancel_handlers(msg: types.Message, state: FSMContext):
    try:
        cur_state = await state.get_state()
        if cur_state is None:
            return
    finally:
        await state.finish()
        await msg.reply('Отмена')
    


def register_client_handlers():
    dp.register_message_handler(load_settings, commands=['settings'], state=None)
    dp.register_message_handler(load_from_lang, state=FSMAdmin.lang_from)
    dp.register_message_handler(load_to_lang, state=FSMAdmin.lang_to)
    dp.register_message_handler(do_translate, state=FSMAdmin.translate)
    dp.register_message_handler(cancel_handlers, commands=['cancel', 'Отмена'], state='*')
    dp.register_message_handler(cancel_handlers, Text(equals='отмена', ignore_case=True), state='*')
