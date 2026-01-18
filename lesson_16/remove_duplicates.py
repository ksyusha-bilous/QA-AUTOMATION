import csv
from pathlib import Path

# Шляхи до вхідних CSV-файлів
file1 = Path("lesson_16/random-michaels.csv")
file2 = Path("lesson_16/random.csv")

data = []          # список для зберігання всіх рядків з обох файлів
header = None      # змінна для збереження заголовка (беремо лише один раз)

# Проходимося по обох файлах
for file in [file1, file2]:
    # Відкриваємо файл у режимі читання
    with file.open(newline='', encoding='utf-8') as f:
        reader = csv.reader(f)

        # Зчитуємо перший рядок — це заголовок
        file_header = next(reader)

        # Якщо заголовок ще не збережений — зберігаємо його з першого файлу
        if header is None:
            # strip() прибирає зайві пробіли
            header = [h.strip() for h in file_header]

        # Читаємо всі інші рядки (дані)
        for row in reader:
            # Очищаємо кожну комірку від пробілів
            clean_row = [cell.strip() for cell in row]

            # Перевіряємо, що рядок не порожній
            if any(clean_row):
                data.append(clean_row)

# Видаляємо дублікати:
# - перетворюємо кожен рядок у tuple (щоб можна було покласти в set)
# - set автоматично прибирає дублікати
# - повертаємо назад у список списків
unique_data = list(map(list, {tuple(row) for row in data}))

# Шлях до результуючого файлу
result_file = Path("lesson_16/result_Bilous.csv")

# Записуємо результат у новий CSV-файл
with result_file.open('w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    # Записуємо заголовок лише один раз
    writer.writerow(header)

    # Записуємо всі унікальні рядки
    writer.writerows(unique_data)

# Повідомлення про успішне виконання
print(f"Результат записано у {result_file}")
