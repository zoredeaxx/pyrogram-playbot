from pyrogram import Client
from app.vars import var

BOT = Client(
    session_name= ':memory:',
    api_id=var.API_ID,
    api_hash=var.API_HASH,
    bot_token=var.BOT_TOKEN,
    sleep_threshold=var.SLEEP_THRESHOLD,
    workers=var.WORKERS
)
