from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse
import json

app = FastAPI()
connections = []

@app.get("/")
async def get():
    return FileResponse('public/index.html')

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)
    number = 0
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            number += 1
            response = f"{number}: {message['message']}"
            for connection in connections:
                await connection.send_text(response)
    except:
        connections.remove(websocket)
