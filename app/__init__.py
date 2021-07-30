import time
from pyrogram import Client
from app.config import var

StartTime = time.time()
plugins = dict(
    root = "app/plugins"
)

bot = Client(
    session_name=':memory:',
    api_id=var.API_ID,
    api_hash=var.API_HASH,
    bot_token=var.BOT_TOKEN,
    workers=var.WORKERS,
    plugins=plugins
)