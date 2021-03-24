import requests

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


def test_get_method_return_full_list_of_video_from_table():
    stubber1 = {
        'id': 1,
        "title": "Intégral de Cabrel",
        "views": 1,
        "likes": 1,
    }
    response = requests.get((BASE_URL + 'video'))
    print("response : ", response.json())
    
    assert response.json()[0] == stubber1

def test_post_method_signup_activate():
    response = requests.post(BASE_URL + "/signup/activate/test1")
    assert response.json() == "test1"
