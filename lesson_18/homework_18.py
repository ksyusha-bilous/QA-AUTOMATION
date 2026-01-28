# 1. Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
def even_numbers(N):
    for i in range(0, N+1, 2):
        yield i

for n in even_numbers(10):
    print("1.Task:", n)
# for i in range(0, N+1, 2) — перебирає всі парні числа від 0 до N
# yield i — повертає наступне число, зупиняє функцію до наступного виклику
# Після останнього числа генератор автоматично піднімає StopIteration



# 2.Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci_generator(N):
    a, b = 0, 1 # a та b -  перші числа ряду Фібоначчі
    while a <= N:
        yield a
        a, b = b, a + b

# Приклад використання:
N = 20
for num in fibonacci_generator(N):
    print (f"2.Task- послідовність Фібоначчі: {num}")



#3. Реалізуйте ітератор для зворотного виведення елементів списку.
numbers = [1, 2, 3, 4]
# створюємо ітератор по перевернутому списку
it = iter(numbers[::-1])  # [4, 3, 2, 1]

while True:
    try:
        n = next(it) # next(it) — дістає по одному елементу
        print("3.Task.Виводимо елементи у зворотньому порядку:",n)
    except StopIteration:
        break


# 4. Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenNumbers:
    def __init__(self, N):
        self.N = N
        self.current = 0  # починаємо з 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.N:
            raise StopIteration
        value = self.current
        self.current += 2  # наступне парне число. тобто +2
        return value
    
for n in EvenNumbers(9):
   print(f"4.Task: {n}")



# 5.Напишіть декоратор, який логує аргументи та результати викликаної функції.
def log_decorator(func):
    def wrapper(*args, **kwargs):
        # Логування аргументів
        print(f"5.Task Виклик функції: {func.__name__}")
        print(f"Позиційні аргументи: {args}")
        print(f"Іменовані аргументи: {kwargs}")

        # Виклик оригінальної функції
        result = func(*args, **kwargs)

        # Логування результату
        print(f"Результат: {result}\n")
        return result
    return wrapper

# Використання

@log_decorator
def add(a, b):
    return a + b

@log_decorator
def greet(name, greeting="Привіт"):
    return f"{greeting}, {name}!"

# Виклики функцій
add(5, 3)  # тільки позиційні аргументи
greet("Оксана")  # іменований аргумент за замовчуванням
greet("Іван", greeting="Доброго дня")  # явний іменований аргумент

# 6.Створіть декоратор, який перехоплює та обробляє винятки, які виникають в 
# ході виконання функції.
def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            # Виклик оригінальної функції
            return func(*args, **kwargs)
        except Exception as e:
            # Обробка винятку
            print(f"Виникла помилка у функції '{func.__name__}': {e}")
            # Можна повернути значення за замовчуванням або None
            return None
    return wrapper

# Приклад використання

@exception_handler
def divide(a, b):
    return a / b

@exception_handler
def greet(name):
    return f"Привіт, {name}!"

# Виклики функцій
print(divide(10, 2))   # нормальний виклик, результат 5.0
print(divide(5, 0))    # помилка ділення на нуль, декоратор перехоплює виняток
print(greet("Оксана")) # нормальний виклик, результат "Привіт, Оксана!"
