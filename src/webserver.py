import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import logger
from library import RADIOS
from worker import QUEUE

_logger = logger.init_logger(__name__)
app = FastAPI(title="Raspberry Radio")
templates = Jinja2Templates(directory="src/templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    stations = [(key, data["id"]) for key, data in RADIOS.items()]
    return templates.TemplateResponse(
        "radio.html",
        {
            "request": request,
            "stations": stations,
            "selected_station": None,
        },
    )


@app.post("/", response_class=HTMLResponse)
async def form_post(request: Request, radio_station: str = Form(...)):
    _logger.info(f"Requested: {radio_station}")
    QUEUE.put(radio_station)
    stations = [(key, data["id"]) for key, data in RADIOS.items()]
    return templates.TemplateResponse(
        "radio.html",
        {
            "request": request,
            "stations": stations,
            "selected_station": radio_station,
        },
    )


class Webserver:
    @staticmethod
    def run():
        uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
