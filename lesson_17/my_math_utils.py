def square(x):
    """Повертає квадрат числа"""
    return x ** 2

def cube(x):
    """Повертає куб числа"""
    return x ** 3

def sum_numbers(a, b):
    return a + b

result = sum_numbers(3, 5)
print(result)


def is_even(number):
    return number % 2 == 0

print(is_even(4))
print(is_even(7))



def max_number(a, b):
    if a > b:
        return a
    else:
        return b