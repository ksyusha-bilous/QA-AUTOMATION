# sqlite3_app.py
# Створення моделі даних: Створіть просту модель даних для системи управління студентами. 
# Модель може містити таблиці для студентів, курсів та їх відношень. Кожен студент може бути 
# зареєстрований на декілька курсів. Наприклад, створити 5 курсів, та розподілити рандомно 20 
# студентів.
# Виконання базових операцій: Напишіть програму, яка додає нового студента до бази даних та 
# додає його до певного курсу. Переконайтеся, що ці зміни коректно відображаються у базі даних.
# Запити до бази даних: Напишіть запити до бази даних, які повертають інформацію про студентів, 
# зареєстрованих на певний курс, або курси, на які зареєстрований певний студент.
# Оновлення та видалення даних: Реалізуйте можливість оновлення даних про студентів або курси, 
# а також видалення студентів з бази даних.
import random
import sqlite3

DB = "students_sqlite3.db"
# connect(host="localhost", port=5432, user="...", password="...")

def create_tables(conn: sqlite3.Connection):
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")

# Створення таблиці students
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        );
    """)
# Створення таблиці courses
    cur.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL UNIQUE
        );
    """)
# Створення таблиці зв'язків Many-to-Many
    cur.execute("""
        CREATE TABLE IF NOT EXISTS enrollments (
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            PRIMARY KEY (student_id, course_id),
            FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE,
            FOREIGN KEY(course_id) REFERENCES courses(id) ON DELETE CASCADE
        );
    """)
    conn.commit() # обов'язково  зберегти зміни

#Заповнення тестових даних (seed)
def seed(conn: sqlite3.Connection):
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM courses;")
    if cur.fetchone()[0] > 0:
        return

    courses = ["Math", "Physics", "Databases", "Python", "DevOps"]
    cur.executemany("INSERT INTO courses(title) VALUES (?);", [(t,) for t in courses])

    # 20 студентів
    for i in range(1, 21):
        name = f"Student {i}"
        email = f"student{i}@mail.com"
        cur.execute("INSERT INTO students(name, email) VALUES (?, ?);", (name, email))
        student_id = cur.lastrowid  # cur.lastrowid дає id щойно вставленого студента.

        # 1..3 курсов
        cur.execute("SELECT id FROM courses;")
        course_ids = [row[0] for row in cur.fetchall()]
        chosen = random.sample(course_ids, k=random.randint(1, 3))

        cur.executemany(
            "INSERT OR IGNORE INTO enrollments(student_id, course_id) VALUES (?, ?);", #INSERT OR IGNORE — не вставляє дублікат, якщо такий зв’язок вже є.
            [(student_id, cid) for cid in chosen],
        )

    conn.commit()

#Додавання нового студента на курс
def add_student_to_course(conn: sqlite3.Connection, name: str, email: str, course_title: str):
    cur = conn.cursor()

    cur.execute("SELECT id FROM courses WHERE title = ?;", (course_title,))
    row = cur.fetchone()
    if not row:
        print("No such course:", course_title)
        return
    course_id = row[0]

    cur.execute("INSERT INTO students(name, email) VALUES (?, ?);", (name, email))
    student_id = cur.lastrowid

    cur.execute(
        "INSERT INTO enrollments(student_id, course_id) VALUES (?, ?);",
        (student_id, course_id),
    )
    conn.commit()
    print("Added:", student_id, name, "->", course_title)

#Запити до бази - Хто на певному курсі:
def students_in_course(conn: sqlite3.Connection, course_title: str):
    cur = conn.cursor()
    cur.execute("""
        SELECT s.id, s.name, s.email
        FROM students s
        JOIN enrollments e ON e.student_id = s.id
        JOIN courses c ON c.id = e.course_id
        WHERE c.title = ?
        ORDER BY s.id;
    """, (course_title,))
    return cur.fetchall()

#Запити до бази - На які курси записаний студент:
def courses_of_student(conn: sqlite3.Connection, email: str):
    cur = conn.cursor()
    cur.execute("""
        SELECT c.id, c.title
        FROM courses c
        JOIN enrollments e ON e.course_id = c.id
        JOIN students s ON s.id = e.student_id
        WHERE s.email = ?
        ORDER BY c.id;
    """, (email,))
    return cur.fetchall()

#ОНОВЛЕННЯ та ВИДАЛЕННЯ
def update_student_email(conn: sqlite3.Connection, student_id: int, new_email: str):
    cur = conn.cursor()
    cur.execute("UPDATE students SET email = ? WHERE id = ?;", (new_email, student_id))
    conn.commit()
    print("Updated student email:", student_id, "->", new_email)


def update_course_title(conn: sqlite3.Connection, old_title: str, new_title: str):
    cur = conn.cursor()
    cur.execute("UPDATE courses SET title = ? WHERE title = ?;", (new_title, old_title))
    conn.commit()
    print("Updated course title:", old_title, "->", new_title)


def delete_student(conn: sqlite3.Connection, student_id: int):
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = ?;", (student_id,))
    conn.commit()
    print("Deleted student:", student_id)


if __name__ == "__main__":
    random.seed(42) #Рандомні курси для студентів завжди будуть одні й ті ж, якщо seed = 42.
    conn = sqlite3.connect(DB) # Підключення до БД
    create_tables(conn) #створює таблиці students, courses, enrollments (якщо їх ще немає).
    seed(conn) #наповнює базу тестовими даними: 5 курсів і 20 студентів, призначає їх на курси випадково.


   #Додавання нового студента на курс
    add_student_to_course(conn, "New Student", "new@student.com", "Databases") 

    print("\nStudents in Databases:")
    for row in students_in_course(conn, "Databases"):
        print(row)

    print("\nCourses of new@student.com:")
    print(courses_of_student(conn, "new@student.com"))

    # найдем id нового студента
    cur = conn.cursor()
    cur.execute("SELECT id FROM students WHERE email = ?;", ("new@student.com",))
    new_id = cur.fetchone()[0]

    update_student_email(conn, new_id, "new2@student.com")
    update_course_title(conn, "Python", "Advanced Python")
    delete_student(conn, new_id)

    conn.close() #Закриття з’єднання з БД
