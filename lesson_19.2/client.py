import requests

BASE_URL = "http://127.0.0.1:8080"

# -----------------------------
# 1️⃣ POST /upload
# -----------------------------
file_path = "image555.jpg" 
with open(file_path, "rb") as f:  #Відкриваємо файл у режимі читання байтів
    files = {"image": f}  #files- словник, де ключ — ім’я поля (в app.py це 'image'), а значення — об’єкт файлу.
    response = requests.post(f"{BASE_URL}/upload", files=files)

if response.status_code == 201:
    upload_data = response.json()# .json() перетворює JSON-відповідь сервера у Python словник.
    image_url = upload_data["image_url"]#Сервер повертає  JSON {"image_url": "http://127.0.0.1:8080/uploads/image555.jpg"}. Ми дістаємо URL через ключ "image_url"
    print("Файл завантажено:", image_url)
else:
    print("Помилка завантаження:", response.status_code, response.text)
    exit() # припиняє виконання скрипта у випадку якщо файл не завантажено.

# -----------------------------
# 2️⃣ GET /image/<filename> для отримання JSON із URL
# -----------------------------
filename = image_url.split("/")[-1] #метод .split("/") розбиває рядок на список частин,
#розділених символом /.  [-1] це звернення до останнього елементу списку, тобто  'image555.jpg'


# Встановлюємо Content-Type: text, бо сервер саме це очікує для JSON
get_response = requests.get(
    f"{BASE_URL}/image/{filename}",
    headers={"Content-Type": "text"}
)

if get_response.status_code == 200:
    image_data = get_response.json()
    print("Отримано URL через GET:", image_data["image_url"])
else:
    print("Помилка GET:", get_response.status_code, get_response.text)

# -----------------------------
# 3️⃣ DELETE /delete/<filename>
# -----------------------------
delete_response = requests.delete(f"{BASE_URL}/delete/{filename}") # видалення файлу

if delete_response.status_code == 200:
    delete_data = delete_response.json()
    print("Файл видалено:", delete_data["message"])
else:
    print("Помилка видалення:", delete_response.status_code, delete_response.text)

