import uvicorn
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

from raspberry_radio.logger import init_logger
from raspberry_radio.worker import QUEUE

_logger = init_logger(__name__)
app = FastAPI(title="Raspberry Radio")


@app.get("/", status_code=200, response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="en">
        <style>
        form {
          margin: 0 auto;
          width: auto;
          text-align: left;
          display: table;
        }
        </style>
        <form name="Radio selection" action="/" method="POST">
            <input type="radio" id="off" name="radio_station" value="Off" checked>
            <label for="off">Off</label><br>

            <input type="radio" id="psr" name="radio_station" value="PSR">
            <label for="psr">Palanga street radio</label><br>

            <input type="radio" id="opus" name="radio_station" value="Opus">
            <label for="opus">LRT Opus</label><br>

            <input type="radio" id="nts1" name="radio_station" value="NTS1">
            <label for="nts1">NTS1</label><br>

            <input type="radio" id="nts2" name="radio_station" value="NTS2">
            <label for="nts2">NTS2</label><br>
            
            <input type="radio" id="rvln" name="radio_station" value="RVLN">
            <label for="nts2">RVLN</label><br>

            <input type="submit">
        </form>
    </html>
    """


@app.post("/")
def form_post(radio_station: str = Form(...)):
    QUEUE.put(radio_station)
    return HTMLResponse(read_root())


class Webserver:
    @staticmethod
    def run():
        uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
