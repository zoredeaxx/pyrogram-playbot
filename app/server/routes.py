import time
from aiohttp import web
from ..bot import BOT
from app import StartTime
from ..utils.time_format import get_readable_time
routes = web.RouteTableDef()


@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response({"status": "running",
                              "uptime": get_readable_time(time.time() - StartTime),
                              "telegram_bot": '@'+(await BOT.get_me()).username})
