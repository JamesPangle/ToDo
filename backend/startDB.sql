drop table if exists items;
drop table if exists lists;

CREATE TABLE if not exists lists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE if not exists items (
    item_id SERIAL PRIMARY KEY,
    list_id INTEGER REFERENCES Lists(id),
    descr TEXT UNIQUE NOT NULL,
    due DATE,
    completed BOOLEAN DEFAULT FALSE
);



