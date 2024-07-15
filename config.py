# (©)CodeXBotz

import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7466932121:AAE2PE-EOt-MdxrfygWaxvrV7WtQkwB_zBA")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29726755"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0a708211226ff747f38c47a80a5e29c0")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002182002460"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6995317382"))

# Port
PORT = int(os.environ.get("PORT", "8080"))

# Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://arfin01:Arkaku123@cluster0.s2drx4p.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

# Force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001863480442"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002101999638"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1002207753207"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "0"))

# Number of workers
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")

# Admins list
try:
    ADMINS = [int(x) for x in os.environ.get("ADMINS", "").split()]
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

# Set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "False").lower() in ['true', '1', 't', 'y', 'yes']

# Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "False").lower() in ['true', '1', 't', 'y', 'yes']

# Bot stats text
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"

# User reply text
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

# Adding owner and another admin to the admin list
ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

# Log file name
LOG_FILE_NAME = "filesharingbot.txt"

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
