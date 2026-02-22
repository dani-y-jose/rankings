create table places
(
    name        TEXT,
    location    TEXT,
    country     TEXT,
    city        TEXT,
    category_id integer
        constraint places_categories_id_fk
            references categories,
    id          integer not null
        constraint places_pk
            primary key autoincrement
);

