#ІМПОРТИ ВБУДОВАНИХ МОДУЛІВ
# 1.Потрібно вивести корінь квадратний числа та вивести на друк число пі
import math
number = 25

print("Квадратний корінь з 25:", math.sqrt(number))
print("Число π:", math.pi)


#2. Виведи  поточну дату
from datetime import datetime
now = datetime.now()
print("Поточна дата:", now)


#3.Створи список чисел від 1 до 10. Випадково обери одне число зі списку. Виведи його у консоль
from random import *
list = [45, 66,-99, 69, 9877, 0, 55,44, 35676,-765]
list_1 = choice (list)
print("3.Рандомне число:", list_1)


#4.Отримай поточну робочу директорію.Виведи її у консоль
import os as o
cwd = o.getcwd()  # getcwd() повертає шлях до поточної директорії
print("Поточна директорія:", cwd)

#5.Виведи у консоль версію Python, яку ти зараз використовуєш
import sys as s
print(f"Поточна версія Python: {s.version}")

#6.Імпортуй модуль calendar.Виведи на екран календар на поточний місяць.
#Перевір, чи рік 2026 є високосним, і виведи результат у консоль.

import calendar
from datetime import date

# Поточний рік і місяць
today = date.today() #дізнаємось сьогоднішню дату.
year = today.year #витягуємо рік із цієї дати.
month = today.month #витягуємо місяць із цієї дати.

# Виведення календаря на поточний місяць
print(calendar.month(year, month))

# Перевірка, чи рік високосний
is_leap = calendar.isleap(year)
print(f"{year} високосний рік: {is_leap}")


#7. Попросіть користувача ввести своє ім’я користувача.
#Попросіть користувача ввести пароль, так щоб його не було видно при введенні.
#Виведіть у консоль повідомлення: Логін: <ім'я>
#Пароль введено успішно!

from getpass import *

# Користувач вводить ім'я
username = input("Введіть своє ім'я: ")

# Користувач вводить пароль (не буде видно під час введення)
password = getpass("Введіть пароль: ")

# Вивід результату
print(f"Логін: {username}")
print("Пароль введено успішно!")


#ІМПОРТИ ІНСТАЛЬОВАНИХ МОДУЛІВ
#8. Створи масив чисел від 1 до 10 та виведи суму елементів.

import numpy as np

arr = np.arange(1, 11)
print(f"8.Масив: {arr}")
print(f"Сума елементів: {np.sum(arr)}")

#9. Імпортуй лише array з numpy та створи масив із трьох чисел.
from numpy  import  array
number = array([1, 2, 3])
print (f" 9. Масив:{number}")

#10.Імпортуй Fore з colorama і виведи текст червоним кольором.
from colorama import Fore, Style

text = Fore.RED + "Hello World" + Style.RESET_ALL #Fore — це набір констант кольорів, не функція.
print(text)

#11. Імпортуй Faker, створи обʼєкт і виведи випадкове імʼя.
from faker import *

fake = Faker()
print(fake.name()) #name() — метод, який повертає випадкове імʼя (рядок)


#12. Імпортуй pytz та виведи список доступних часових зон (перші 5).
from pytz import *
# Доступні всі часові зони з all_timezones
# Беремо перші 5 за допомогою зрізу [:5]
first_5_timezones = all_timezones[:5]

print(f"12. Перші 5 доступних часових зон: {first_5_timezones}")


#13.Імпортуй  rich і виведи слово Hello жирним шрифтом.
import rich

rich.print("[bold]13.Hello[/bold]")

#14. Створи список списків data, де кожен підсписок містить ім’я та вік людини.
#Використовуючи tabulate, виведи дані у вигляді красивої таблиці з заголовками "Name" та "Age".
#Вибери формат таблиці "grid" для оформлення сітки.
import tabulate
data = [
    ["Alice", 25],
    ["Bob", 30],
    ["Charlie", 22]
]
print(tabulate.tabulate(data, headers=["Name", "Age"], tablefmt="grid"))


#ІМПОРТИ ВЛАСНИХ МОДУЛІВ
#15. Імпорт  з файлу my_utils
import my_utils

print(my_utils.greet("Oksana"))
print("Значення PI:", my_utils.PI)

#16. Імпорт функції square з файлу my_math_utils.py
from  my_math_utils import square
res_1= square(6)
print (f"16.Квадрат  заданого числа:{res_1}")


#17. Імпорт функції cube з файлу my_math_utils.py
from  my_math_utils import cube
print(f"17. Куб заданого числа: {cube(3)}")


#18. Імпорт функції sum_numbers з файлу my_math_utils.py
from my_math_utils import *

result = sum_numbers(3, 5)
print(f"18 Сума чисел = {result}")


#19. Імпорт функції is_evens з файлу my_math_utils.py
import my_math_utils  as m
print(m.is_even(4))
print(m.is_even(7))

#20.Імпорт функції max_number з файлу my_math_utils.py
import my_math_utils  as m

result = m.max_number(7, 10)
print(result)
