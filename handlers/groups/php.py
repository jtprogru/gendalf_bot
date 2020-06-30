import random
from aiogram import types

from data.config import ADMIN_LIST
from loader import dp


@dp.message_handler(regexp='(php|PHP)')
async def group_bot_php(message: types.Message):
    if message.from_user.id not in ADMIN_LIST:
        username = message.from_user.username
        text = [
            f'Тут <a href=\"https://t.me/@{username}\">{username}</a> хочет получить трындюлей за ПеХаПе\n',
            f'Кто говорит про ПеХаПе, тот Филип Киркоров!',
        ]

        await message.reply(
            text=random.choice(text),
            parse_mode=types.ParseMode.HTML,
        )
    else:
        username = message.from_user.username
        text = f'<a href=\"https://t.me/@{username}\">{username}</a> ' \
               f'ты это, аккуратнее, а то покажу где раком зимуют...\n'

        await message.reply(
            text=text,
            parse_mode=types.ParseMode.HTML,
        )
