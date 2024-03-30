

from starlette.testclient import TestClient

from .config import Settings
from .main import app, get_settings

client = TestClient(app)

def get_settings_override():
    settings = {
        "app_name": "Awesome API", "admin_email" : "testing_admin@example.com", "items_per_user" :10
    }
    print(*settings)
    return Settings(**settings)


app.dependency_overrides[get_settings] = get_settings_override


def test_app():
    response = client.get("/info")
    data = response.json()

    print("Testing")
    assert data == {
        "app_name": "Awesome API",
        "admin_email": "testing_admin@example.com",
        "items_per_user": 10,
    }
