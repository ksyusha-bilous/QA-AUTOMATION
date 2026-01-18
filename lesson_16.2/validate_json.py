import json
import logging
from pathlib import Path

# Шлях до папки з JSON-файлами
json_dir = Path("lesson_16.2")

# Шлях до лог-файлу (у тій самій папці)
log_file = json_dir / "json__Bilous.log"

# Налаштування логера
logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Перебір усіх json-файлів у папці
for file in json_dir.glob("*.json"):
    try:
        with file.open(encoding="utf-8") as f:
            json.load(f)  # перевірка валідності JSON
    except json.JSONDecodeError as e:
        logging.error(f"Файл {file.name} невалідний JSON: {e}")
    except Exception as e:
        logging.error(f"Помилка при обробці файлу {file.name}: {e}")

print("Перевірка JSON-файлів завершена")
