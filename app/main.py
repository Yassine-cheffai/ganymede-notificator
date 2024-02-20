from fastapi import FastAPI
from app.models import Notification


app = FastAPI()


@app.post("/")
async def notify(notification: Notification):
    return {
        "message": f"sending message to {notification.to}, of type {notification.notification_type}"
    }
