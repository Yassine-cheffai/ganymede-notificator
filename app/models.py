from pydantic import BaseModel, field_validator

from app.constants import NOTIFICATION_TYPES


class Notification(BaseModel):
    to: str
    notification_type: str

    @field_validator("to")
    def to_must_be_valid_email(cls, value):
        if not "@" in value:
            raise ValueError("email is not is the correct format")
        return value

    @field_validator("notification_type")
    def type_must_be_correct(cls, value):
        if not value.upper() in NOTIFICATION_TYPES:
            raise ValueError("not a valid notification type")
        return value
