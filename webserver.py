from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import uvicorn
from worker import QUEUE

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
            <input type="radio" id="off" name="radio_station" value="Off">
            <label for="off">Off</label><br>
            
            <input type="radio" id="psr" name="radio_station" value="PSR">
            <label for="psr">Palanga street radio</label><br>
            
            <input type="radio" id="opus" name="radio_station" value="Opus">
            <label for="opus">LRT Opus</label><br>
            
            <input type="radio" id="nts1" name="radio_station" value="NTS1">
            <label for="nts1">NTS1</label><br>
            
            <input type="radio" id="nts2" name="radio_station" value="NTS2">
            <label for="nts2">NTS2</label><br>
            
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