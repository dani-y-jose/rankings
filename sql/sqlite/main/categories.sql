create table categories
(
    name        TEXT,
    description TEXT,
    id          integer not null
        constraint categories_pk
            primary key
);

