import logging
from sqlite3 import Error
from connect import create_connect as connect
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
QUERIES_FOLDER = BASE_DIR / 'queries'
QUERIES_FILES = (item.name for item in QUERIES_FOLDER.iterdir() if item.is_file())

QUERY_DESCRIPTIONS: dict[ str, str ] = {
		'query_01.sql': '5 студентів із найбільшим середнім балом з усіх предметів',
		'query_02.sql': '\nCтудент із найвищим середнім балом з певного предмета.',
		'query_03.sql': '\nCередній бал у групах з певного предмета',
		'query_04.sql': '\nCередній бал на потоці (по всій таблиці оцінок)',
		'query_05.sql': '\nЯкі курси читає певний викладач',
		'query_06.sql': '\nСписок студентів у певній групі',
		'query_07.sql': '\nОцінки студентів у окремій групі з певного предмета',
		'query_08.sql': '\nСередній бал, який ставить певний викладач зі своїх предметів',
		'query_09.sql': '\nСписок курсів, які відвідує студент',
		'query_10.sql': '\nСписок курсів, які певному студенту читає певний викладач',
		'query_11.sql': '\nСередній бал, який певний викладач ставить певному студентові.',
		'query_12.sql': '\nОцінки студентів у певній групі з певного предмета на останньому занятті.',
		}


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


def file_red(path: Path) -> str:
	with open(path, 'r') as f:
		sql = f.read()
	return sql


if __name__ == "__main__":
	for file in QUERIES_FILES:
		if file in QUERY_DESCRIPTIONS:
			print(QUERY_DESCRIPTIONS[file])

		else:
			print("Відсутній опис для цього файлу")

		path = QUERIES_FOLDER / file
		select_query = file_red(path)
		slect_db(select_query)
