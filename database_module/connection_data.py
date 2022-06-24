DB_NAME = 'hw_storage'

POSTGRES_CONNECTION_DATA = dict(
    host='localhost',
    database=DB_NAME,
    user='postgres',
    password='postgres',
    port='5432',
)

MYSQL_CONNECTION_DATA = dict(
    host='localhost',
    user='mysqluser',
    password='mysqlpassword',
    database=DB_NAME,
)

MYSQL_TABLE_FIELDS = {
    'customers': ('customer_id', 'full_name', 'address'),
    'suppliers': ('supplier_id', 'company_name', 'phone_number'),
    'hardwares': ('hardware_id', 'supplier_id', 'item_name'),
    'purchases': ('purchase_id', 'customer_id', 'hardware_id'),
}