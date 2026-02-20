create table products
(
    name        TEXT,
    category_id integer
        constraint products_categories_id_fk
            references categories,
    id          integer not null
        constraint products_pk
            primary key autoincrement
);

