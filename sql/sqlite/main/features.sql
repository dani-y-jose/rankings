create table features
(
    name       TEXT,
    product_id integer
        constraint features_products_id_fk
            references products,
    id         integer not null
        constraint features_pk
            primary key autoincrement
);

