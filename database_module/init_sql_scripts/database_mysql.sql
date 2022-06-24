drop table if exists purchases cascade;
drop table if exists hardwares cascade;
drop table if exists suppliers cascade;
drop table if exists customers cascade;


create table customers (
    customer_id int auto_increment primary key,
    full_name text not null,
    address text not null
);

create table suppliers (
    supplier_id int auto_increment primary key,
    company_name text not null,
    phone_number text not null
);

create table hardwares (
    hardware_id int auto_increment primary key,
    supplier_id int,
    item_name text not null,
    foreign key (supplier_id) references suppliers(supplier_id)
);

create table purchases (
    purchase_id int auto_increment primary key,
    customer_id integer,
    hardware_id integer,
    foreign key (customer_id) references customers(customer_id),
    foreign key (hardware_id) references hardwares(hardware_id)
);