from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_missing_key():
    response = client.post("/predict_icd", json={})
    assert response.status_code == 400


def test_missing_request():
    response = client.post("/predict_icd", json=None)
    assert response.status_code == 422
