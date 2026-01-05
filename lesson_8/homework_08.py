"""Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал". 
Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
який дозволяє змінювати середній бал студента. 
Виведіть інформацію про студента та змініть його середній бал."""

class Student:
    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def info(self):
         return (f"Name: {self.name}, "
                f"Surname: {self.surname}, "
                f"Age: {self.age}, "
                f"Average grade: {self.average_grade}")
    

    def set_grade(self, new_grade = 0):
        self.average_grade = new_grade
        return f"Average grade was changed to {self.average_grade}."
    

student_1 = Student("Oksana", "Bilous", age=20, average_grade=90)


print(student_1.info())
print(student_1.set_grade(95))
print(student_1.info())




