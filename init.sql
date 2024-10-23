CREATE TABLE soda_results
(
    id SERIAL NOT NULL PRIMARY KEY,
    creation_date timestamp NOT NULL default CURRENT_TIMESTAMP,
    results TEXT
);
