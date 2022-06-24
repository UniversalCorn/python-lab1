import os
import sqlite3
from database_module import SQL_DIR, CACHE_DIR

DB_INIT_SCRIPT = 'database_sqlite3.sql'
DB_FILE_NAME = 'hw_storage.sqlite3'


class SQLite:
    def __init__(self, file=f'{CACHE_DIR}/{DB_FILE_NAME}'):
        self.file = file

    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        # self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()


def init_hw_sqlite_db():
    os.remove(f'{CACHE_DIR}/{DB_FILE_NAME}')
    with SQLite() as cur:
        with open(f'{SQL_DIR}/{DB_INIT_SCRIPT}') as sql:
            cur.executescript(sql.read())
