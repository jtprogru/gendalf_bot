from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit

from data.config import ADMIN_LIST


@rate_limit(55, 'help')
@dp.message_handler(CommandHelp())
async def user_bot_help(message: types.Message):
    if message.from_user.id in ADMIN_LIST:
        text = [
            'Список команд: ',
            '/start - Начать диалог',
            '/help - Получить справку',
            '/ban - Забанить',
            '/unban - Разбанить',
            '/ping - Тест бота',
            '/report - Пожаловаться на мудака',
            '/pics - Получить картинку',
        ]
        await message.reply('\n'.join(text))
    else:
        text = [
            'Список команд: ',
            '/start - Начать диалог',
            '/help - Получить справку',
            '/ping - Тест бота',
            '/report - Пожаловаться на мудака',
            '/pics - Получить картинку',
        ]
        await message.reply('\n'.join(text))
