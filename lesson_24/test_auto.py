import requests
import pytest
import logging

BASE_URL = "http://127.0.0.1:8080"

# ----------------- Логування -----------------
logger = logging.getLogger("car_tests")
logger.setLevel(logging.INFO)

# Очищаємо старі обробники
logger.handlers = []

# Логування у файл
fh = logging.FileHandler("test_search.log", mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

# Логування у консоль
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)

# Щоб pytest пропускав логування у консоль
logger.propagate = True

# ----------------- Фікстура авторизації -----------------
@pytest.fixture(scope="class")
def login():
    logger.info("Авторизація користувача...")
    r = requests.post(f"{BASE_URL}/auth", auth=("test_user", "test_pass"))
    assert r.status_code == 200, "Не вдалося авторизуватися"
    token = r.json()["access_token"]
    logger.info("Авторизація успішна. Токен отримано.")
    return token

# ----------------- Тести -----------------
def test_get_cars(login):
    logger.info("Виконується тест: test_get_cars")
    r = requests.get(f"{BASE_URL}/cars", headers={"Authorization": f"Bearer {login}"})
    logger.info(f"Статус код: {r.status_code}, Кількість машин: {len(r.json())}")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    assert len(r.json()) == 25

def test_get_cars_limit(login):
    limit = 5
    logger.info(f"Виконується тест: test_get_cars_limit (limit={limit})")
    r = requests.get(f"{BASE_URL}/cars", headers={"Authorization": f"Bearer {login}"}, params={"limit": limit})
    logger.info(f"Кількість машин: {len(r.json())}")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    assert len(r.json()) == limit

def test_get_sort_by_year(login):
    sort_by = "year"
    logger.info(f"Виконується тест: test_get_sort_by_year (sort_by={sort_by})")
    r = requests.get(f"{BASE_URL}/cars", headers={"Authorization": f"Bearer {login}"}, params={"sort_by": sort_by})
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    data = r.json()
    for i in range(len(data)-1):
        assert data[i][sort_by] <= data[i+1][sort_by]

def test_get_sort_by_price_limit(login):
    sort_by = "price"
    limit = 7
    logger.info(f"Виконується тест: test_get_sort_by_price_limit (sort_by={sort_by}, limit={limit})")
    r = requests.get(f"{BASE_URL}/cars", headers={"Authorization": f"Bearer {login}"}, params={"sort_by": sort_by, "limit": limit})
    assert r.status_code == 200
    data = r.json()
    logger.info(f"Кількість машин: {len(data)}")
    assert len(data) == limit
    for i in range(len(data)-1):
        assert data[i][sort_by] <= data[i+1][sort_by]

def test_get_cars_brand(login):
    logger.info("Виконується тест: test_get_cars_brand (перевірка бренду першої машини)")
    r = requests.get(f"{BASE_URL}/cars", headers={"Authorization": f"Bearer {login}"})
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert "brand" in data[0]
    logger.info(f"Перший автомобіль: {data[0]}")