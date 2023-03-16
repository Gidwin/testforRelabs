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
    while True:
        data = await websocket.receive_text()
        message = json.loads(data)
        response = message['message']
        await websocket.send_text(response)
