GRANT ALL PRIVILEGES ON DATABASE "flask" TO "postgres";


CREATE TABLE flask (
    ID uuid PRIMARY KEY,
    flask_column varchar(100) NOT NULL
);
