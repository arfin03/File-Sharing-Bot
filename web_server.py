# web_server.py

from aiohttp import web

async def web_server():
    async def handle(request):
        return web.Response(text="Hello, this is a web server for the bot!")
    
    app = web.Application()
    app.router.add_get('/', handle)
    return app
