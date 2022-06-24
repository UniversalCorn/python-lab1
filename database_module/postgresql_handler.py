import psycopg2
from database_module.connection_data import POSTGRES_CONNECTION_DATA
from database_module import SQL_DIR

DB_INIT_SCRIPT = 'database_postgresql.sql'

class Postgres:
    def __enter__(self):
        self.conn = psycopg2.connect(**POSTGRES_CONNECTION_DATA)
        self.conn.autocommit = True
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

def init_hw_pg_db():
    with Postgres() as cur:
        with open(f'{SQL_DIR}/{DB_INIT_SCRIPT}') as sql:
            cur.execute(sql.read())


if __name__ == "__main__":
    init_hw_pg_db()
