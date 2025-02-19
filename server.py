from fastapi import FastAPI, WebSocket
import random

app = FastAPI()

# Sample AI responses (Replace with real AI logic)
AI_RESPONSES = [
    "Hello! How can I assist you?",
    "I'm just a simple AI. What do you need?",
    "That’s interesting! Tell me more.",
    "I don't know everything, but I can try to help!",
    "Can you elaborate on that?",
]

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("AI: Welcome! Start chatting...")

    while True:
        try:
            data = await websocket.receive_text()  # Receive user message
            ai_response = random.choice(AI_RESPONSES)  # Simulated AI response
            await websocket.send_text(f"AI: {ai_response}")  # Send response
        except:
            await websocket.close()
            break