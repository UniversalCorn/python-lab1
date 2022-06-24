from database_module.sqlite3_handler import SQLite



class Entity:
    def __init__(self, table_name, pk_name, fields_to_add):
        self.table_name = table_name
        self.pk_name = pk_name
        self.fields_to_add = fields_to_add


    def create(self, *args) -> int:
        with SQLite() as cur:
            fields = ', '.join(self.fields_to_add)
            values = "'" + "', '".join(args) + "'"
            cur.execute(f'''insert into {self.table_name} ({fields})
                            values ({values})''')
            return cur.lastrowid


    def get_all(self):
        with SQLite() as cur:
            result = cur.execute(f'''select * from {self.table_name}''').fetchall()
            return result


    def delete(self, pk: int):
        with SQLite() as cur:
            cur.execute(f'''delete from {self.table_name} where {self.pk_name}={pk}''')
            return pk


class CustomersEntity(Entity):
    def __init__(self):
        super().__init__(
            table_name='customers',
            pk_name='customer_id',
            fields_to_add=['full_name', 'address', 'email']
        )

    def create(self, full_name, address, email) -> int:
        return super().create(full_name, address, email)


class SuppliersEntity(Entity):
    def __init__(self):
        super().__init__(
            table_name='suppliers',
            pk_name='supplier_id',
            fields_to_add=['company_name', 'phone_number']
        )

    def create(self, company_name, phone_number) -> int:
        return super().create(company_name, phone_number)


class HardwaresEntity(Entity):
    def __init__(self):
        super().__init__(
            table_name='hardwares',
            pk_name='hardware_id',
            fields_to_add=['supplier_id', 'item_name', 'price', 'amount']
        )

    def create(self, supplier_id, item_name, price, amount) -> int:
        return super().create(supplier_id, item_name, price, amount)


class PurchasesEntity(Entity):
    def __init__(self):
        super().__init__(
            table_name='purchases',
            pk_name='purchase_id',
            fields_to_add=['customer_id', 'hardware_id', 'amount', 'total_price']
        )

    def create(self, customer_id, hardware_id, amount, total_price) -> int:
        return super().create(customer_id, hardware_id, amount, total_price)



class DBAdmin:
    def __init__(self):
        self.customers = CustomersEntity()
        self.suppliers = SuppliersEntity()
        self.hardwares = HardwaresEntity()
        self.purchases = PurchasesEntity()
        self.entities = {
            'customers': self.customers,
            'suppliers': self.suppliers,
            'hardwares': self.hardwares,
            'purchases': self.purchases,
        }

