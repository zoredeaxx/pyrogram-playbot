from app.bot import BOT
from app.vars import var
from pyrogram import filters

@BOT.on_message(filters.command('start'))
async def start(bot, message):
    await message.reply("Hello! You reached Pyrogram Playbot.")
