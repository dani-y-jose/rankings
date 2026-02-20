create table stars
(
    feature_id integer not null
        constraint stars_features_id_fk
            references features,
    review_id  integer not null
        constraint stars_reviews_id_fk
            references reviews,
    value      REAL    not null,
    id         integer not null
        constraint stars_pk
            primary key
);

