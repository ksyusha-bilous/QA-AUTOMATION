"""Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
 Напишіть код, який свормує новий list (наприклад lst2), 
 який містить лише змінні типу стрінг, які присутні в lst1. 
 Данні в лісті можуть бути будь якими"""

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = [x for x in lst1 if isinstance(x, str)]
print(lst2)


#isinstance(x, str) перевіряє, чи є x рядком (str).
#Лист-компрехеншн [x for x in lst1 if ...] формує новий список тільки з потрібних елементів.