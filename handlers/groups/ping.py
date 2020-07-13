from aiogram import types
from loader import dp


@dp.message_handler(commands=['ping'])
async def user_bot_start(message: types.Message):
    text = f'<b>pong</b>'
    await message.answer(
        text=text,
        parse_mode=types.ParseMode.HTML,
        disable_web_page_preview=True,
        reply=True,
    )
