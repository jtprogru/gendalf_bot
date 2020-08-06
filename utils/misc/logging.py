import logging
import sentry_sdk
from sentry_sdk.integrations.aiohttp import AioHttpIntegration
from data.config import SENTRY_DSN

sentry_sdk.init(dsn=SENTRY_DSN, integrations=[AioHttpIntegration()])
logging.basicConfig(
    format=u"%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s",
    # level=logging.INFO,
    level=logging.DEBUG,
)
