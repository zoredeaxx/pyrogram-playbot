import sys
import glob
import asyncio
import logging
import importlib
from pathlib import Path
from pyrogram import idle
from app.bot import BOT
from app.vars import var
from aiohttp import web
from app.server import web_server
from app.utils.keepalive import ping_server
from apscheduler.schedulers.background import BackgroundScheduler

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("apscheduler").setLevel(logging.WARNING)

ppath = "app/bot/plugins/*.py"
files = glob.glob(ppath)

loop = asyncio.get_event_loop()

async def start_services():
    print('\n')
    print('------------------- Initalizing Telegram Bot -------------------')
    await BOT.start()
    print('----------------------------- DONE -----------------------------')
    print('\n')
    print('-------------------- Importing All Plugins ---------------------')
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            plugins_dir = Path(f"app/bot/plugins/{plugin_name}.py")
            import_path = ".plugins.{}".format(plugin_name)
            spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
            sys.modules["app.bot.plugins." + plugin_name] = load
            print("Imported => " + plugin_name)
    print('----------------------------- DONE -----------------------------')
    print('\n')
    if var.ON_HEROKU and var.KEEP_ALIVE:
        print('------------------ Starting Keep-Alive Service ------------------')
        print('Platform Detected => Heroku')
        scheduler = BackgroundScheduler()
        scheduler.add_job(ping_server, "interval", seconds=1200)
        scheduler.start()
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
    print('Bot => {}'.format((await BOT.get_me()).first_name))
    print('Server IP => {}:{}'.format(var.BIND_ADRESS, var.PORT))
    print('App Runnng On => {}'.format(var.URL))
    print('---------------------------------------------------------------')
    await idle()

if __name__ == '__main__':
    loop.run_until_complete(start_services())
