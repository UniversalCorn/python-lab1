import psycopg2

from database_module.sqlite3_handler import SQLite
from database_module.postgresql_handler import Postgres
from database_module.mysql_handler import MySQL
from database_module import TABLE_NAMES
from database_module.connection_data import MYSQL_TABLE_FIELDS
from database_module.postgresql_handler import init_hw_pg_db


def migrate_sqlite_to_pg():
    init_hw_pg_db()
    with SQLite() as sqlite_cur, Postgres() as pg_cur:
        for table_name in TABLE_NAMES:
            rows = sqlite_cur.execute(f'SELECT * FROM {table_name}').fetchall()
            try:
                for row in rows:
                    pg_cur.execute(f'INSERT INTO {table_name} VALUES {row}')
            except psycopg2.Error as e:
                print(e)



def migrate_pg_to_mysql():
    with Postgres() as pg_cur, MySQL() as my_cur:
        for table_name in TABLE_NAMES:
            fields = ', '.join(MYSQL_TABLE_FIELDS[table_name])
            pg_cur.execute(f'SELECT {fields} FROM {table_name}')
            rows = pg_cur.fetchall()
            my_cur.execute(f'SET FOREIGN_KEY_CHECKS=0')
            my_cur.execute(f'truncate table {table_name}')
            my_cur.execute(f'SET FOREIGN_KEY_CHECKS=1')
            for row in rows:
                my_cur.execute(f'INSERT INTO {table_name}({fields}) VALUES {row}')

        # update rows
        for pk in (1, 2, 3):
            my_cur.execute(f'''update customers set address = concat('updated ', address) where customer_id = {pk}''')
            my_cur.execute(
                f'''update suppliers set company_name = concat('updated ', company_name) where supplier_id = {pk}''')
            my_cur.execute(
                f'''update hardwares set item_name = concat('updated ', item_name) where hardware_id = {pk}''')


