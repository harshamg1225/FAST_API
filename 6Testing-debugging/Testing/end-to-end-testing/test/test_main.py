from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_eligibility_pass():

    response = client.post(
        "/loan-eligibility",
        json={"income": 60000, "age": 24, "employment_status": "Employed"},
    )

    assert response.status_code == 200
    assert response.json() == {"elligibility": True}


def test_eligibility_fail():

    response = client.post(
        "/loan-eligibility",
        json={"income": 20000, "age": 15, "employment_status": "Employed"},
    )

    assert response.status_code == 200
    assert response.json() == {"elligibility": False}
