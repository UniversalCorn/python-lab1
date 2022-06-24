import mysql.connector
from database_module.connection_data import MYSQL_CONNECTION_DATA
from database_module.connection_data import DB_NAME
from database_module import SQL_DIR

DB_INIT_SCRIPT = 'database_mysql.sql'


class MySQL:
    def __enter__(self):
        self.conn = mysql.connector.connect(**MYSQL_CONNECTION_DATA)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()


def recreate_mysql_db():
    with MySQL() as cur:
        cur.execute(f'drop database if exists {DB_NAME}')
        cur.execute(f'create database {DB_NAME}')


def init_hw_mysql_db():
    with MySQL() as cur:
        with open(f'{SQL_DIR}/{DB_INIT_SCRIPT}') as sql:
            cur.execute(sql.read(), multi=True)


if __name__ == '__main__':
    init_hw_mysql_db()
