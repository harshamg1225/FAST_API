from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch


client = TestClient(app)


def test_predict_with_out_mock():

    response = client.post(
        "/Predition",
        json={
            "SepalLengthCm": 6.6,
            "SepalWidthCm": 3,
            "PetalLengthCm": 5.2,
            "PetalWidthCm": 3,
        },
    )

    assert response.status_code == 200
    assert response.json() == {"predicted": 2}


def test_predict_with_mock():

    with patch("model.Model.predict") as mock_predict:
        mock_predict.return_value = [1]

        response = client.post(
            "/Predition",
            json={
                "SepalLengthCm": 6.6,
                "SepalWidthCm": 3,
                "PetalLengthCm": 5.2,
                "PetalWidthCm": 3,
            },
        )

        assert response.status_code == 200
        assert response.json() == {"predicted": 1}
