from aiogram import types

from loader import dp
from utils.pics import local_image, unsplashed_img


@dp.message_handler(commands=["pics"])
async def group_bot_pics(message: types.Message):
    pic_name = unsplashed_img()
    with open(pic_name, "rb") as photo:
        await message.reply_photo(photo)
