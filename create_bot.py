from aiogram import Bot
from aiogram.dispatcher import Dispatcher


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
