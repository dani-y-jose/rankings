create table reviews
(
    place_id    integer not null
        constraint reviews_places_id_fk
            references places,
    product_id  integer not null
        constraint reviews_products_id_fk
            references products,
    timestamp   TEXT,
    comments    TEXT,
    reviewer_id integer not null
        constraint reviews_reviewers_id_fk
            references reviewers,
    id          integer not null
        constraint reviews_pk
            primary key autoincrement
);

