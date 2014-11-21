CREATE TABLE user (
        id INTEGER NOT NULL,
        username VARCHAR(80),
        email VARCHAR(120),
        password VARCHAR(120),
        registered_on DATETIME,
        last_login DATETIME,
        PRIMARY KEY (id),
        UNIQUE (username),
        UNIQUE (email)
);

