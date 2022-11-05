from aiogram.utils import executor

from create_bot import dp

from handlers import client

async def on_startup(_):
    print('Filia-san is ready to work')


if __name__ == '__main__':
    client.register_client_handlers()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
