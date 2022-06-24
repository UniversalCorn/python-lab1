-- sqlite 3
PRAGMA foreign_keys = ON;

drop table if exists customers;
drop table if exists suppliers;
drop table if exists hardwares;
drop table if exists purchases;

create table customers (
    customer_id integer primary key autoincrement,
    full_name text not null,
    address text not null,
    email text
);

insert into customers (full_name, address, email) values ('gena', 'zp', 'g@e.com');
insert into customers (full_name, address, email) values ('kolya', 'dp', 'k@e.com');
insert into customers (full_name, address, email) values ('vitya', 'rv', 'v@e.com');
insert into customers (full_name, address, email) values ('petya', 'kv', 'p@e.com');
insert into customers (full_name, address, email) values ('rostik', 'vl', 'r@e.com');

create table suppliers (
    supplier_id integer primary key autoincrement,
    company_name text not null,
    phone_number text not null
);

insert into suppliers (company_name, phone_number) values ('intel', '+10001112233');
insert into suppliers (company_name, phone_number) values ('amd', '+10001112234');
insert into suppliers (company_name, phone_number) values ('nvidia', '+10001112235');
insert into suppliers (company_name, phone_number) values ('techcomp', '+10001112236');


create table hardwares (
    hardware_id integer primary key autoincrement,
    supplier_id integer,
    item_name text not null,
    price real not null,
    amount integer not null,
    foreign key (supplier_id) references suppliers(supplier_id)
);

insert into hardwares (supplier_id, item_name, price, amount) values (1, 'i9-9900k', 10000.0, 5);
insert into hardwares (supplier_id, item_name, price, amount) values (2, 'fx-8300', 20000.0, 5);
insert into hardwares (supplier_id, item_name, price, amount) values (3, 'rtx3090', 30000.0, 5);
insert into hardwares (supplier_id, item_name, price, amount) values (4, 'some_detail', 15000.0, 5);


create table purchases (
    purchase_id integer primary key autoincrement,
    customer_id integer,
    hardware_id integer,
    amount integer not null,
    total_price real not null,
    foreign key (customer_id) references customers(customer_id),
    foreign key (hardware_id) references hardwares(hardware_id)
);

insert into purchases (customer_id, hardware_id, amount, total_price) values (1, 1, 2, 20000);
insert into purchases (customer_id, hardware_id, amount, total_price) values (2, 2, 2, 40000);
insert into purchases (customer_id, hardware_id, amount, total_price) values (3, 3, 2, 60000);
insert into purchases (customer_id, hardware_id, amount, total_price) values (4, 4, 2, 30000);