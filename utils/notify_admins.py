import logging

from aiogram import Dispatcher

from data.config import ADMIN_LIST


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMIN_LIST:
        try:
            await dp.bot.send_message(
                chat_id=int(admin),
                text="Бот Запущен"
            )

        except Exception as err:
            logging.exception(err)
