import sqlite3
from contextlib import contextmanager
from pathlib import Path

DATABASE = Path('study_group.db').absolute()

@contextmanager
def create_connect(db_filt: Path = DATABASE):
    conn = sqlite3.connect(db_filt)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()