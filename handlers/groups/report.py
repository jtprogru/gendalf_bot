from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp
from data.config import MASTER_ADMIN_ID


@dp.message_handler(Command(["report"]))
async def user_bot_help(message: types.Message):
    """
    Отправка сообщения в чат и админу в личку о том, что кто-то мудак
    """
    from_name = message.from_user.username
    username = message.reply_to_message.from_user.username
    text = [
        f'Пользователь <a href="https://t.me/@{from_name}">{from_name}</a>\n',
        f'Сказал что мудак у нас <a href="https://t.me/@{username}">{username}</a>',
    ]
    await message.answer(text="\n".join(text), parse_mode=types.ParseMode.HTML)
    await message.bot.send_message(
        chat_id=MASTER_ADMIN_ID, text="\n".join(text), parse_mode=types.ParseMode.HTML
    )
