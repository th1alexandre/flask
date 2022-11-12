GRANT ALL PRIVILEGES ON DATABASE "flask" TO "postgres";


CREATE TABLE table_a (
    ID uuid PRIMARY KEY,
    column_a varchar(100) NOT NULL,
    column_b integer NOT NULL
);

CREATE TABLE table_b (
    ID uuid PRIMARY KEY,
    column_a boolean,
    column_b timestamp UNIQUE
);
