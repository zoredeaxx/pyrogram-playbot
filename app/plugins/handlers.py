from pyrogram import Client, filters

@Client.on_message(filters.command('start'))
def start_handler(_, msg):
    msg.reply("Hello! You\'ve reached **Pyrogram Playbot**")