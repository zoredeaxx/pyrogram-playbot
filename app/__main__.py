import sys
from pyrogram import idle
from asyncio import get_event_loop
from aiohttp import web
from app.server import web_server
from app import bot
from app.config import var

loop = get_event_loop()

async def start_services():
    print('\n')
    print('------------------- Initalizing Telegram Bot -------------------')
    await bot.start()
    print('----------------------------- DONE -----------------------------')
    print('\n')
    print('-------------------- Initalizing Web Server --------------------')
    app = web.AppRunner(await web_server())
    await app.setup()
    try:
        await web.TCPSite(app, var.BIND_ADRESS, var.PORT).start()
    except:
        sys.exit("Couldn\'t bind the app on specified host or port. Please check if the specified host is valid for your machine and make sure the port is empty.")
    print('----------------------------- DONE -----------------------------')
    print('\n')
    print('----------------------- Service Started -----------------------')
    print('Bot => {} (@{})'.format((await bot.get_me()).first_name, (await bot.get_me()).username))
    print('Server IP => {}:{}'.format(var.BIND_ADRESS, var.PORT))
    print('App Runnng On => {}'.format(var.URL))
    print('---------------------------------------------------------------')
    await idle()

if __name__ == '__main__':
    loop.run_until_complete(start_services())