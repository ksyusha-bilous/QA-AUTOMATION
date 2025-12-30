
# task 1
#Написати функцію, яка обчислює суму двох чисел.
def summ (a,b):
    return a+b

# result = summ (3, 6)
# print (f"Сума двох чисел: {result}")



# task 2
#Написати функцію, яка розрахує середнє арифметичне списку чисел.
def average (numbers):
    return sum(numbers) / len (numbers)

# nums = [2,4,5,790,33,55,-2]
# result = average (nums)
# print (f"Середнє арифметичне списку чисел: {result}")



# task 3
#Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
def  longest_word (words):
    if not words:
        return None
    return max (words,key=len) #max(вбудована функція) бере максимальний елемент за довжиною слова, бо key=len
# words1 =['bshf','hfwhsfwsfh','ggg', 'ggyggg']
# result = longest_word (words1)
# print (result)


