import requests
import pytest

BASE_URL = "http://127.0.0.1:5000/"


def test_get_method_return_first_video_from_table():
    stubber = {
        'id': 1,
        "title": "Intégral de Cabrel",
        "views": 1,
        "likes": 1,
    }
    response = requests.get(BASE_URL + 'video/%d' % 1)
    print("response : ", response.json())
    assert response.json() == stubber

