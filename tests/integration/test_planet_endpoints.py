from http import HTTPStatus

from fastapi.testclient import TestClient


def test_conditions_list(client: TestClient):
    """Test planet conditions response.

    Args:
        client: TestClient - test client.
    """
    response = client.get('/planet/all_conditions')
    assert response.status_code == HTTPStatus.OK

    conditions = response.json()['conditions']

    assert isinstance(conditions, list)


def test_predict(client: TestClient, sample_image_bytes: bytes):
    """Test predict response.

    Args:
        client: TestClient - test client.
        sample_image_bytes: bytes - image.
    """
    files = {
        'image': sample_image_bytes,
    }
    response = client.post('/planet/predict', files=files)

    assert response.status_code == HTTPStatus.OK

    predicted_conditions = response.json()['conditions']

    assert isinstance(predicted_conditions, list)


def test_predict_proba(client: TestClient, sample_image_bytes: bytes):
    """Test predict probability response.

    Args:
        client: TestClient - test client.
        sample_image_bytes: bytes - image.
    """
    files = {
        'image': sample_image_bytes,
    }
    response = client.post('/planet/predict_proba', files=files)

    assert response.status_code == HTTPStatus.OK

    probs = response.json()

    for prob in probs['conditions'].values():
        assert prob <= 1
        assert prob >= 0
