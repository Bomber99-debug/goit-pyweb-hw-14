from pathlib import Path
from connect import DATABASE, create_connect as connect

CREATE_FOLDER = Path(__file__).parent / 'create_tables'
CREATE_FILES = (
		'create_1.sql',
		'create_2.sql',
		'create_3.sql',
		'create_4.sql',
		'create_5.sql',
		)


def create_db(path_folder: Path, create_files: tuple, path_database: Path) -> None:
	with connect(path_database) as conn:
		cur = conn.cursor()

		for file in create_files:
			path = path_folder / file
			with open(path, 'r') as f:
				sql = f.read()
			cur.executescript(sql)


def main() -> None:
	create_db(CREATE_FOLDER, CREATE_FILES, DATABASE)


if __name__ == "__main__":
	main()
