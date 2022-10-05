#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5475114115:AAEsCFspBUh81SgyhpzzkDdtFgwaMrRQ3J8")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "12225868"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "ba4a6dfd31791f14316312a46584437b")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "AgC6jUwAakRWwjb8xXcpB2oGKXltoo7DdAyxidg3g0-IgZQc8ReKzzrKkWgc7xfkm8Nfb30j-txIPFEMn6nlScGVZ4vGBZLOmJBKAtXjmHxqAmD25hinl4_zlImV9P0XkEnTjciOJThiNnFANcCYb0Y1PSPUBKUXqBcyoIRaTvNUh65vAh2_vByNshOQN82UE-GA6d4FfyuPOn3fGE-KQqO_5FplPMrf4wMX55y9hJ7srdsIiAAGr8h7RgSQaZknvDn_nSKpyi04SEyBRpuqwpXMF6GiHJ3pOd5eNp-77tLltz4f00gd-ZZnSDd6a5s0PwXbfkLWOzogGWMoaC2NFEzzlWNlJAAAAAFWiUM4AA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgresql://sery:xtcz1324@localhost:5432/serydb")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
