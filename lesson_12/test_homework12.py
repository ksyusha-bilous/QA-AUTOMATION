import unittest

from homework12 import summ  # імпортуємо функцію з іншого файлу
class TestSumm(unittest.TestCase):

# Кейс 1: додавання позитивних чисел
    def test_positive_numbers(self):
        result = summ(3, 6)
        self.assertEqual(result, 9)  # очікуємо 9

# Кейс 2: додавання від’ємного і позитивного числа
    def test_negative_and_positive(self):
        result = summ(-2, 5)
        self.assertEqual(result, 3)  # очікуємо 3

# Кейс 3: додавання двох від’ємних чисел
    def test_negative_numbers(self):
        result = summ(-4, -6)
        self.assertEqual(result, -10) #очікуємо -10



#Написати функцію, яка розрахує середнє арифметичне списку чисел.
from homework12 import average
class TestAverageFunction(unittest.TestCase):

    # Кейс 1: звичайний список цілих чисел
    def test_average_of_integers(self):
        nums = [2, 4, 6, 8]
        result = average(nums)
        self.assertEqual(result, 5)

    # Кейс 2: список з від’ємними числами (перевірка істинності)
    def test_average_with_negative_numbers(self):
        nums = [10, -10, 10, -10]
        result = average(nums)
        self.assertTrue(result == 0)

    # Кейс 3: дробовий результат (приблизна рівність)
    def test_average_float_result(self):
        nums = [1, 2, 3]
        result = average(nums)
        self.assertAlmostEqual(result, 2.0, places=2) #2.0 - очікуване середнє знач, places=2 - перевірка на рівність до 2 знаків після коми



from homework12 import longest_word  # імпортуємо функцію з іншого файлу

class TestLongestWordFunction(unittest.TestCase):

    # Кейс 1: звичайний список слів
    def test_normal_list(self):
        words = ['bshf','hfwhsfwsfh','ggg', 'ggyggg']
        result = longest_word(words)
        self.assertEqual(result, 'hfwhsfwsfh')  # очікуємо найдовше слово

    # Кейс 2: список з однаковими по довжині словами
    def test_same_length_words(self):
        words = ['cat', 'dog', 'bat']
        result = longest_word(words)
        self.assertIn(result, words)  # будь-яке слово з списку може бути повернуто

    # Кейс 3: список містить одне слово
    def test_single_word(self):
        words = ['hello']
        result = longest_word(words)
        self.assertEqual(result, 'hello')  # повертається саме це слово

    # Кейс 4: порожній список
    def test_empty_list(self):
        words = []
        result = longest_word(words)
        self.assertIsNone(result)  # очікуємо None для порожнього списку


if __name__ == "__main__":
    unittest.main(verbosity=2)














