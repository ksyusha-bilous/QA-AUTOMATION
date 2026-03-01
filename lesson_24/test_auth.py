import requests


BASE_URL = "http://127.0.0.1:8080"

def test_login_success():
    r = requests.post(f"{BASE_URL}/auth", auth=("test_user", "test_pass"))
    assert r.status_code == 200
    response = r.json()
    assert response["access_token"]

def test_login_unsuccess():
    r = requests.post(f"{BASE_URL}/auth", auth=("user", "pass"))
    assert r.status_code == 401


def test_login_not_allowed_method():
    r = requests.get(f"{BASE_URL}/auth", auth=("test_user", "test_pass"))
    assert r.status_code == 405
