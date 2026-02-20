create table places
(
    name     TEXT,
    location TEXT,
    country  TEXT,
    province TEXT,
    id       integer not null
        constraint places_pk
            primary key autoincrement
);

