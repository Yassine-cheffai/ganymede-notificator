from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_bad_email_validation():
    """
    Test that a bad email or bad notification type raise a validation error
    """
    response = client.post("/", data={"to": "test", "notification_type": "welcome"})
    assert response.status_code == 422

    response = client.post(
        "/", data={"to": "test@mail.com", "notification_type": "some_type"}
    )
    assert response.status_code == 422
