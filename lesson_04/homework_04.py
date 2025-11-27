adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;git
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer_new1= adwentures_of_tom_sawer.replace("\n", " ")
print("task01:", adwentures_of_tom_sawer_new1)


# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer_new2 = adwentures_of_tom_sawer.replace("....", " ")
print ("task02:", adwentures_of_tom_sawer_new2)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer_new3 = " ".join(adwentures_of_tom_sawer.split())
print ("TASK03:", adwentures_of_tom_sawer_new3)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = adwentures_of_tom_sawer.count("h")
print("TASK04:", count_h)


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words = adwentures_of_tom_sawer.split() # розбиває текст на слова.
count_capital = sum(1 for w in words if w[0].isupper()) 

print("TASK05:", count_capital)


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

tom_first = adwentures_of_tom_sawer.find("Tom")
if tom_first != -1:
    tom_second = adwentures_of_tom_sawer.find("Tom", tom_first + 1)
    if tom_second != -1:
        print("TASK06: слово Tom вдруге на позиції", tom_second)
    else:
        print("TASK06: слово Tom зустрічається лише один раз")
else:
    print("TASK06: слово Tom не зустрічається в тексті")

  


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
import re
adwentures_of_tom_sawer_new7 = adwentures_of_tom_sawer.replace("....", " ")
print ("task02:", adwentures_of_tom_sawer_new7)
# Розділяємо текст на речення
adwentures_of_tom_sawer_sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z0-9])', adwentures_of_tom_sawer_new7)
# (?<=[.!?]): цей вираз вказує, що потрібно знайти будь-який символ після крапки (.), знака питання (?) або оклику (!).
# \s+: дозволяє пропускати один або більше пробілів (це розмежування між реченнями).
# (?=[A-Z0-9]): Перевіряє, що після пробілу йде або велика літера (A-Z), або цифра (0-9).
# Заміна \n на пробіл у кожному реченні
adwentures_of_tom_sawer_sentences = [sentence.replace("\n", " ") for sentence in adwentures_of_tom_sawer_sentences]
# Виведення результату
print("TASK07:", adwentures_of_tom_sawer_sentences)


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
# Виводимо четверте речення, переведене в нижній регістр
fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
# Виведення результату
print("TASK08:", fourth_sentence)


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
# Перевіряємо, чи починається якесь речення з "By the time"
found = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"): # strip() прибирає  пробіли на початку  та кінці речення, startswith -пошук  на початку 
        found = True
        break
# Виводимо результат
if found:
    print("TASK09: Є речення, яке починається з 'By the time'.")
else:
    print("TASK09: Немає речень, які починаються з 'By the time'.")



# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
# Отримуємо останнє речення
last_sentence = adwentures_of_tom_sawer_sentences[-1]

# Розділяємо останнє речення на слова та рахуємо їх кількість
word_count = len(last_sentence.split())

# Виводимо результат
print("TASK10: Кількість слів в останньому реченні:", word_count)
