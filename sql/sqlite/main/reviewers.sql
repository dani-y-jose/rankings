create table reviewers
(
    name TEXT,
    id   integer not null
        constraint reviewers_pk
            primary key autoincrement
);

