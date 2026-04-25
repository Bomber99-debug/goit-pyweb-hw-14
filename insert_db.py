from fake_data import fake
from connect import DATABASE, create_connect as connect
from random import randint
from datetime import datetime
from pathlib import Path
from itertools import cycle


GROUP = 3
STUDENTS = randint(30, 50)
TEACHERS = randint(3, 5)
SUBJECTS = randint(5, 8)


def generate_fake_data(
    number_groups: int, number_student: int, number_teacher: int, number_subjects: int
):
    fake_groups: set[str] = set()
    fake_student: set[str] = set()
    fake_teacher: set[str] = set()
    fake_subjects: set[str] = set()

    while len(fake_groups) != number_groups:
        fake_groups.add(fake.groups())

    while len(fake_student) != number_student:
        fake_student.add(fake.full_name())

    while len(fake_teacher) != number_teacher:
        fake_teacher.add(fake.full_name())

    while len(fake_subjects) != number_subjects:
        fake_subjects.add(fake.subjects())

    return fake_groups, fake_student, fake_teacher, fake_subjects


def normal_subjects_in_teachers(subjects: set[str], teachers: set[str]) -> list[tuple[str, int]]:
    id_teacher: list[int] = [num for num in range(1, len(teachers)+1)]
    
    return list(zip(subjects, cycle(id_teacher)))
    

def insert_data_to_db(
    groups: set[str], students: set[str], teachers: set[str], subjects: set[str], db_path: Path = DATABASE
) -> None:
    with connect(db_path) as conn:
        cur = conn.cursor()

        sql_to_groups = """
        INSERT INTO groups(group_title)
        VALUES (?)
        """

        cur.executemany(sql_to_groups, [(group,) for group in groups])

        sql_to_teacher = """
        INSERT INTO teachers(fullname)
        VALUES (?)
        """

        cur.executemany(sql_to_teacher, [(teacher,) for teacher in teachers])

        sql_to_students = """
        INSERT INTO students(fullname, group_id)
        VALUES (?, ?)
        """

        cur.executemany(sql_to_students, [(student, randint(1, 3),) for student in students])

        sql_to_subjects = """
        INSERT INTO subjects(title, teacher_id)
        VALUES (?, ?)
        """
        
        cur.executemany(sql_to_subjects, normal_subjects_in_teachers(subjects, teachers))
        
        sql_to_grades="""
        INSERT INTO grades(student_id, subject_id, grade, grade_date)
        VALUES (?, ?, ?, ?)
        """
        
        for _ in range(len(students)**2):
            grade = randint(0, 100)
            if grade != 0:
                date = str(datetime(2024, randint(1,12), randint(1,28)).date())
                cur.execute(sql_to_grades, (randint(1, len(students)), randint(1, len(subjects)), grade, date))
            else:    
                cur.execute(sql_to_grades, (randint(1, len(students)), randint(1, len(subjects)), None, None))
        

if __name__ == "__main__":
    groups, students, teachers, subjects = generate_fake_data(
        number_groups=GROUP,
        number_student=STUDENTS,
        number_teacher=TEACHERS,
        number_subjects=SUBJECTS,
    )


    insert_data_to_db(groups, students, teachers, subjects)
