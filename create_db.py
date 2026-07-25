from pathlib import Path
from connect import DATABASE, create_connect as connect

BASE_DIR = Path(__file__).resolve().parent
CREATES_FOLDER = BASE_DIR / 'create_tables'
CREATES_FILES = (item.name for item in CREATES_FOLDER.iterdir() if item.is_file())


def create_db(path_folder: Path, create_files: tuple, path_database: Path) -> None:
	with connect(path_database) as conn:
		cur = conn.cursor()

		for file in create_files:
			path = path_folder / file
			with open(path, 'r') as f:
				sql = f.read()
			cur.executescript(sql)


def main() -> None:
	create_db(CREATES_FOLDER, CREATES_FILES, DATABASE)


if __name__ == "__main__":
	main()
