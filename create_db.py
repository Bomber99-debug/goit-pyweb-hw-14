from pathlib import Path
from connect import DATABASE, create_connect as connect


CREATE_TABLE = Path('create_table.sql').absolute()


def create_db(path_create: Path, path_database: Path) -> None:
    with open(path_create, 'r') as file:
        sql = file.read()
        
    with connect(path_database) as conn:
        cur = conn.cursor()
        cur.executescript(sql)
        
def main() -> None:
    create_db(CREATE_TABLE, DATABASE)
    
if __name__ == "__main__":
    main()
