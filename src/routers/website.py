from fastapi import APIRouter
from fastapi.responses import HTMLResponse

import config
import website.template

router = APIRouter()

@router.get("/")
def website_main():
    return HTMLResponse(website.template.render_file("index.html.j2"))

@router.get("/word")
def website_word():
    return HTMLResponse(website.template.render_file("word.html.j2"))

