import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
MASTER_ADMIN_ID = str(os.getenv("MASTER_ADMIN_ID"))
ADMIN_LIST = [int(MASTER_ADMIN_ID), ]
LINK_CHAT_RULES = str(os.getenv("LINK_CHAT_RULES"))

ip = os.getenv("REDIS_IP")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
