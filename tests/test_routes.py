from fastapi.testclient import TestClient
import pytest

from app.main import app
from app.utils.parse import get_avg_data

client = TestClient(app)
avg_data = get_avg_data()


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200


def test_read_all_states():
    response = client.get("/states")
    assert response.status_code == 200
    result = response.json()
    assert "Description" in result.keys()
    assert isinstance(result.pop("Description"), str)
    assert all(isinstance(value, float) for value in result.values())


@pytest.mark.parametrize("state", ["NSW", "QLD", "SA", "TAS", "VIC"])
def test_read_state(state: str):
    response = client.get(f"/states/{state}")
    assert response.status_code == 200
    assert response.json() == {
        "state": state,
        "average_price": avg_data[state]
    }


def test_read_invalid_state():
    response = client.get("/states/p")
    assert response.status_code == 400
    assert isinstance(response.json()["detail"], str)
