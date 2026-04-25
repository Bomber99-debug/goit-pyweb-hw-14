import logging
from sqlite3 import Error
from connect import create_connect as connect

def slect_db(select: str) -> None:
    try:
        with connect() as conn:
            if conn is not None:
                c = conn.cursor()
                try:
                    c.execute(select)
                    for result in c.fetchall():
                        print(result) 
                except Error as err:
                    logging.error(err)
                finally:
                    c.close()
            else:
                print("Error! cannot create the database connection.")
    except Error as err:
        logging.error(err)
        
if __name__ == "__main__":
    selct_01 = """
                SELECT
                    s.id,
                    s.fullname,
                    ROUND(AVG(g.grade), 2) AS average_grade
                FROM students s 
                JOIN grades g ON s.id = g.student_id 
                GROUP BY s.id, s.fullname 
                ORDER BY average_grade DESC
                LIMIT 5;
                """
    print("5 студентів із найбільшим середнім балом з усіх предметів")
    slect_db(selct_01)
    
    select_02 = """
                SELECT g.id, s.fullname, s2.title, ROUND(AVG(g.grade), 2) AS avg_grade
                FROM grades g
                JOIN students s ON g.student_id = s.id
                JOIN subjects s2 on g.subject_id  = s2.id 
                WHERE s2.id = 3
                GROUP BY s.id
                ORDER BY avg_grade DESC
                LIMIT 1;
    """
    
    
    print("\nCтудент із найвищим середнім балом з певного предмета.")
    slect_db(select_02)
    
    select_03 = """
                SELECT g2.id, g2.group_title, s2.title, ROUND(AVG(g.grade), 2) AS avg_grade
                FROM grades g
                JOIN students s ON g.student_id = s.id
                JOIN groups g2 ON s.group_id = g2.id
                JOIN subjects s2 on g.subject_id  = s2.id 
                WHERE s2.id = 1
                GROUP BY g2.id
                ORDER BY avg_grade DESC;
    
                """
    
    print("\nCередній бал у групах з певного предмета")
    slect_db(select_03)
    
    select_04 = """
                SELECT ROUND(AVG(g.grade), 2) AS avg_grade
                FROM grades g;
                """
    
    print("\nCередній бал на потоці (по всій таблиці оцінок)")
    slect_db(select_04)
    
    select_05 = """
                SELECT s.title, t.fullname 
                FROM subjects s 
                JOIN teachers t ON s.teacher_id = t.id
                WHERE t.id = 2;
                """
    
    print("\nЯкі курси читає певний викладач")
    slect_db(select_05)
    
    select_06 = """
                SELECT g.group_title, s.fullname  
                FROM students s 
                JOIN groups g ON g.id = s.group_id
                WHERE g.id = 2;
                """
    
    print("\nСписок студентів у певній групі")
    slect_db(select_06)
    
    select_07 = """
                SELECT g2.group_title, s.fullname, g.grade 
                FROM grades g
                JOIN students s ON s.id = g.student_id
                JOIN groups g2 ON g2.id = s.group_id
                JOIN subjects s2 ON s2.id = g.subject_id
                WHERE g2.id = 2 AND s2.id = 2;
                """
    
    print("\nОцінки студентів у окремій групі з певного предмета")
    slect_db(select_07)
    
    select_08 = """
                SELECT t.fullname, s.title, ROUND(AVG(g.grade), 2) AS avg_grade
                FROM grades g
                JOIN subjects s ON s.id = g.subject_id
                JOIN teachers t ON t.id = s.teacher_id
                WHERE t.id = 2
                GROUP BY t.fullname;
                """
    
    print("\nСередній бал, який ставить певний викладач зі своїх предметів")
    slect_db(select_08)
    
    select_09 = """
                SELECT DISTINCT s2.fullname, s.title
                FROM grades g
                JOIN subjects s ON s.id = g.subject_id
                JOIN students s2 ON s2.id = g.student_id 
                WHERE s2.id = 2
                ORDER BY s.title ASC;
                """
    
    print("\nСписок курсів, які відвідує студент")
    slect_db(select_09)
    
    select_10 = """
                SELECT DISTINCT s.title
                FROM grades g
                JOIN subjects s ON s.id = g.subject_id
                JOIN teachers t ON t.id = s.teacher_id
                JOIN students s2 ON s2.id = g.student_id 
                WHERE s2.id = 2 AND t.id =2;
                """
    
    print("\nСписок курсів, які певному студенту читає певний викладач")
    slect_db(select_10)
    
    select_11 = """
                SELECT DISTINCT ROUND(AVG(g.grade))
                FROM grades g
                JOIN subjects s ON s.id = g.subject_id
                JOIN teachers t ON t.id = s.teacher_id
                JOIN students s2 ON s2.id = g.student_id 
                WHERE s2.id = 2 AND t.id =2;
                """
    
    print("\nСередній бал, який певний викладач ставить певному студентові.")
    slect_db(select_11)
    
    select_12 = """
                SELECT g2.group_title, s2.fullname, g.grade, g.grade_date 
                FROM grades g
                JOIN subjects s ON s.id = g.subject_id
                JOIN students s2 ON s2.id = g.student_id 
                JOIN groups g2 ON g2.id = s2.group_id
                WHERE g2.id = 2 AND s.id = 2 AND g.grade_date = (
                    SELECT MAX(g_inner.grade_date) 
                    FROM grades g_inner
                    JOIN students s_inner ON s_inner.id = g_inner.student_id
                    JOIN subjects s2_inner ON s2_inner.id = g_inner.subject_id 
                    WHERE s_inner.group_id = 2 AND s2_inner.id = 2
                );
                """
    
    print("\nОцінки студентів у певній групі з певного предмета на останньому занятті.")
    slect_db(select_12)