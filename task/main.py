from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse
import json

app = FastAPI()

@app.get("/")
async def get():
    return FileResponse('public/index.html')

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    number = 0
    while True:
        data = await websocket.receive_text()
        message = json.loads(data)
        number += 1
        response = {"number": number, "message": message["message"]}
        await websocket.send_json(response)
