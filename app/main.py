from fastapi import FastAPI
from app.models import Notification
import os


app = FastAPI()


@app.post("/")
async def notify(notification: Notification):
    test = os.environ.get("TEST")
    return {
        "message": f"sending message to {notification.to}, of type: {notification.notification_type} - {test}"
    }
