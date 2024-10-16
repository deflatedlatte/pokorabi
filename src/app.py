import json

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

import config
import routers.api
import routers.website

config.initialize_app_config()

app = FastAPI()
app.include_router(
    routers.api.router,
    prefix="/api"
)

landing_page = """<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <p>
            The administrator has disabled built-in web UI for Pokorabi.
        </p>
    </body>
</html>
"""

if config.app_config.use_internal_website():
    app.include_router(routers.website.router)
    app.mount("/static", StaticFiles(directory="static"), name="static")
else:
    @app.get("/")
    def mainpage():
        return HTMLResponse(landing_page)
