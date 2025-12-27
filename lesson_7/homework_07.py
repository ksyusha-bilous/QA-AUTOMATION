# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1

    while number * multiplier <= 25:
        print(f"{number}x{multiplier}={number * multiplier}")
        multiplier += 1 #збільшує змінну на 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
#Написати функцію, яка обчислює суму двох чисел.
def summ (a,b):
    return a+b

result = summ (3, 6)
print (f"Сума двох чисел: {result}")



# task 3
#Написати функцію, яка розрахує середнє арифметичне списку чисел.
def average (numbers):
    return sum(numbers) / len (numbers)

nums = [2,4,5,790,33,55,-2]
result = average (nums)
print (f"Середнє арифметичне списку чисел: {result}")


# task 4
#Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
def reverse_string(s):
    return s[::-1] #slice - зріз від кінця до початку, крок -1

# Користувач вводить рядок
a = ("task 4 рядок ")

# Виклик функції і вивід результату
reversed_text = reverse_string(a)
print("Рядок у зворотному порядку:", reversed_text)



# task 5
#Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
def  longest_word (words):
    if not words:
        return None
    return max (words,key=len) #max(вбудована функція) бере максимальний елемент за довжиною слова, бо key=len
words1 =['bshf','hfwhsfwsfh','ggg', 'ggyggg']
result = longest_word (words1)
print (result)


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    index =str1.find (str2)
    return (index)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
#Порахуйте периметр фігури та виведіть його для користувача
# storona_1 = 1
# storona_2 = 2
# storona_3 = 3
# storona_4 = 4
# perimeter = storona_1 + storona_2 + storona_3 + storona_4
# print("P:", perimeter)
def perimetr (storona_1, storona_2, storona_3, storona_4):
    return sum ([storona_1, storona_2, storona_3, storona_4])

p = perimetr(1, 2, 3, 4)
print("Perimetr:", p)


# Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
# apples = 2
# banana = 4 * apples
# print (apples)
# print (banana)

def count_bananas (banana):
    return banana*4
b=7
result = count_bananas(b)
print (result)


"""Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який сформує новий list (наприклад lst2), 
який містить лише змінні типу стрінг, які присутні в lst1. 
Данні в лісті можуть бути будь якими"""

# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
# lst2 = [x for x in lst1 if isinstance(x, str)]
# print(lst2)

#isinstance(x, str) перевіряє, чи є x рядком (str).
#Лист-компрехеншн [x for x in lst1 if ...] формує новий список тільки з потрібних елементів.

def filter_strings(lst):
    return [x for x in lst if isinstance(x, str)]

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = filter_strings(lst1)

print(lst2)



# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
# lst= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum_even = sum(x for x in lst if x % 2 == 0)
# print(sum_even)

def sum_even (lst):
    return sum(x for x in lst if x % 2 == 0)

lst_a= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (sum_even (lst_a))