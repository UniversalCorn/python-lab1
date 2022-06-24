import os

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
SQL_DIR = f'{THIS_DIR}/init_sql_scripts/'
CACHE_DIR = f'{THIS_DIR}/database_cache/'
TABLE_NAMES = ['customers', 'suppliers', 'hardwares', 'purchases']