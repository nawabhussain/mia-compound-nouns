from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_missing_key():
    response = client.post("/predict_icd", json={})
    assert response.status_code == 400


def test_missing_request():
    response = client.post("/predict_icd", json=None)
    assert response.status_code == 422


def test_icd_code_zungengrundkarzinom():
    response = client.post("/predict_icd", json={'text': 'Zungengrundkarzinom'})
    assert response.status_code == 200
    assert response.json() == {'icd_code': 'C01'}


def test_icd_code_karzinom_des_zungengrundes():
    response = client.post("/predict_icd", json={'text': 'Karzinom des Zungengrundes'})
    assert response.status_code == 200
    assert response.json() == {'icd_code': 'C01'}
