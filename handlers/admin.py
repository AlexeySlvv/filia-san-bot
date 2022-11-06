from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types

from create_bot import dp

from keyboards import kb_lang

from lang_dict import LANG_DICT

class FSMAdmin(StatesGroup):
    lang_from = State()
    lang_to = State()


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
    
    async with state.proxy() as data:
        await msg.reply(str(data))

    await state.finish()


def register_client_handlers():
    dp.register_message_handler(load_settings, commands=['settings'], state=None)
    dp.register_message_handler(load_from_lang, state=FSMAdmin.lang_from)
    dp.register_message_handler(load_to_lang, state=FSMAdmin.lang_to)
