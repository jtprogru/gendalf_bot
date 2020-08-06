from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp
from data.config import ADMIN_LIST, MASTER_ADMIN_ID


@dp.message_handler(Command(["ban"]))
async def user_bot_ban(message: types.Message):
    # TODO: Валидация на админа: Только админ может отправлять нахер
    if message.reply_to_message.from_user.id in ADMIN_LIST:
        username = message.reply_to_message.from_user.username
        text = [f'Забанен <a href="https://t.me/@{username}">{username}</a>']

        await message.bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            permissions=types.ChatPermissions(
                can_send_messages=False, can_send_other_messages=False,
            ),
        )

        await message.bot.send_message(
            chat_id=MASTER_ADMIN_ID,
            text="\n".join(text),
            parse_mode=types.ParseMode.HTML,
        )


@dp.message_handler(Command(["unban"]))
async def user_bot_unban(message: types.Message):
    # TODO: Валидация на админа: Только админ может отправлять нахер
    if message.reply_to_message.from_user.id in ADMIN_LIST:
        username = message.reply_to_message.from_user.username
        text = [f'Разбанен <a href="https://t.me/@{username}">{username}</a>']

        await message.bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            permissions=types.ChatPermissions(
                can_send_messages=True, can_send_other_messages=True,
            ),
        )
        for ADMIN_ID in ADMIN_LIST:
            await message.bot.send_message(
                chat_id=ADMIN_ID, text="\n".join(text), parse_mode=types.ParseMode.HTML
            )
