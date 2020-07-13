from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp


@dp.message_handler(Text(equals="привет", ignore_case=True))
@dp.message_handler(Text(equals="привет!", ignore_case=True))
@dp.message_handler(Text(equals="привет.", ignore_case=True))
async def group_bot_not_hello(message: types.Message):
    username = message.from_user.username
    text = f'Дорогой <a href=\"https://t.me/@{username}\">{username}</a>, ' \
           f'а прочти ка ты для начала <a href=\"https://neprivet.ru\">непривет</a> и ' \
           f'<a href=\"https://nometa.xyz\">nometa</a>, а ' \
           f'потом поговорим...'

    await message.reply(
        text=text,
        parse_mode=types.ParseMode.HTML,
        disable_web_page_preview=True,
    )
