from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_bad_email_validation():
    """
    Test that a bad email raise a validation error
    """
    response = client.post("/", data={"to": "test", "notification_type": "test_type"})
    assert response.status_code == 422
