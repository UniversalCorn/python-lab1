drop table if exists customers cascade;
drop table if exists suppliers cascade;
drop table if exists hardwares cascade;
drop table if exists purchases cascade;

create table customers (
    customer_id serial primary key,
    full_name text not null,
    address text not null,
    email text
);

create table suppliers (
    supplier_id serial primary key,
    company_name text not null,
    phone_number text not null
);

create table hardwares (
    hardware_id serial primary key,
    supplier_id integer,
    item_name text not null,
    price real not null,
    amount integer not null,
    foreign key (supplier_id) references suppliers(supplier_id)
);

create table purchases (
    purchase_id serial primary key,
    customer_id integer,
    hardware_id integer,
    amount integer not null,
    total_price real not null,
    foreign key (customer_id) references customers(customer_id),
    foreign key (hardware_id) references hardwares(hardware_id)
);