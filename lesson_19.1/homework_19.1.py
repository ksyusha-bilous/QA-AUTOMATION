
# Є відкритий офіційний API NASA Images and Video Library ( https://images-api.nasa.gov ), 
# який дозволяє виконувати пошук медіа та отримувати список файлів (assets) для кожного знайденого медіа-елемента.

# Ваше завдання - за допомогою модуля requests:

# Виконати пошук зображень, пов’язаних з ровером Curiosity на Марсі.
# З JSON відповіді витягнути nasa_id для знайдених елементів.
# Для кожного nasa_id зробити додатковий запит до endpoint-а /asset/{nasa_id}, щоб отримати список URL-ів файлів.
# Обрати з цього списку посилання на JPG-зображення (наприклад, перший .jpg або “найкращий” варіант, якщо їх кілька).
# Скачати 2 зображення і зберегти локально як:
# mars_photo1.jpg
# mars_photo2.jpg
# Важливо: потрібно виконати мінімум 3 HTTP-запити:

# 1 запит /search + 2 запити /asset/{nasa_id} (і ще 2 запити на скачування jpg-файлів).

# Доступні endpoint-и (Images API)

# GET /search?q={q} - пошук медіа
# GET /asset/{nasa_id} - список файлів (URL) для вибраного медіа

import requests

BASE_URL = "https://images-api.nasa.gov"

# 1️⃣ Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}

search_response = requests.get(search_url, params=search_params) # 
search_response.raise_for_status() # Це перевірка, чи запит пройшов успішно.

search_data = search_response.json()

# 2️⃣ Отримуємо nasa_id
items = search_data["collection"]["items"]
nasa_ids = [item["data"][0]["nasa_id"] for item in items]

print("Знайдені nasa_id:", nasa_ids[:2]) #nasa_ids[:2] - беремо 2 перші елементи 

# 3️⃣ Шаблон URL для assets
asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"

downloaded = 0

for nasa_id in nasa_ids:
    if downloaded >= 2:
        break

    # 4️⃣ Запит до /asset/{nasa_id}
    asset_url = asset_url_template.format(nasa_id=nasa_id) # format підставляє конкретний nasa_id у URL
    asset_response = requests.get(asset_url) # відправляємо запит
    asset_response.raise_for_status() #Це перевірка, чи запит пройшов успішно.

    asset_data = asset_response.json() # Парсинг JSON-відповіді: Перетворює JSON-відповідь у Python-словник
    urls = asset_data["collection"]["items"] # Отримуємо список файлів (assets)

    # 5️⃣ Пошук JPG
    jpg_urls = [
        item["href"]
        for item in urls
        if item["href"].lower().endswith(".jpg")
    ]

    if not jpg_urls:  #якщо список порожній - то пропустити цей nasa_id і перейти до наступного
        continue

    jpg_url = jpg_urls[0] # беремо перший JPG тільки якщо список непорожній

    # 6️⃣ Скачування зображення
    image_response = requests.get(jpg_url)
    image_response.raise_for_status()

    filename = f"mars_photo{downloaded + 1}.jpg"
    with open(filename, "wb") as f: # "wb" → write binary, запис у бінарному режимі (важливо для зображень!)
        f.write(image_response.content)

    print(f"Збережено: {filename}")
    downloaded += 1
