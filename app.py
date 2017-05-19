import asyncio

from sanic import Sanic

import uvloop

from config import config
from endpoints import add_blueprints


app = Sanic("replay_parsing")


@app.listener('before_server_start')
async def main(app, loop):
    await config(app, loop)
    add_blueprints(app)

if __name__ == "__main__":
    # Use uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    app.run(host="0.0.0.0", port=9999)
