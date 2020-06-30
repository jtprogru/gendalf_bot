from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

from data.config import LINK_CHAT_RULES


@dp.message_handler(CommandStart())
async def user_bot_start(message: types.Message):
    username = message.from_user.username
    text = f'<b>Привет, <a href=\"https://t.me/@{username}\">{username}</a>\n' \
           f'Правила чата <a href=\"{LINK_CHAT_RULES}\">тут</a></b>\n'
    await message.reply(
        text=text,
        parse_mode=types.ParseMode.HTML,
        disable_web_page_preview=True,
    )
