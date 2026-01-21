# Для файла groups.xml створіть функцію пошуку 
# по group/number і повернення значення timingExbytes/incoming 
# результат виведіть у консоль через логер на рівні інфо

import logging
import xml.etree.ElementTree as ET
from pathlib import Path



# Файл XML
xml_file = Path("lesson_16.3/groups.xml")

# --- Ручне налаштування логера ---
logger = logging.getLogger("xml_logger")  # створюємо свій логер
logger.setLevel(logging.INFO)  # рівень логування

# Хендлер для консолі
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Формат повідомлень
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

# Додаємо хендлер до логера
logger.addHandler(console_handler)
# -----------------------------------

def log_incoming_for_all_groups():
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Проходимо по всіх <group> у кореневому елементі
    for group in root.findall("group"):
        number_elem = group.find("number")
        # Шукаємо тег <number> у поточній групі

        if number_elem is not None:
            # Перевіряємо, чи тег <number> існує
            number_value = number_elem.text
            # Беремо текстове значення з <number> (наприклад "0", "1" тощо)

            timing = group.find("timingExbytes")
            # Шукаємо тег <timingExbytes> у поточній групі

            if timing is not None:
                # Перевіряємо, чи тег <timingExbytes> існує
                incoming = timing.find("incoming")
                # Шукаємо тег <incoming> всередині <timingExbytes>

                if incoming is not None:
                    # Якщо <incoming> існує, виводимо його значення
                    logger.info(f"Значення incoming для number={number_value}: {incoming.text}")
                else:
                    # Якщо <incoming> немає, повідомляємо про відсутність
                    logger.info(f"Не знайдено incoming для number={number_value}")
            else:
                # Якщо <timingExbytes> немає, повідомляємо про відсутність
                logger.info(f"Не знайдено timingExbytes для number={number_value}")

# Виконується тільки при запуску скрипта
if __name__ == "__main__":
    log_incoming_for_all_groups()
