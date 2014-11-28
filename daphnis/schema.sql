PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE tag (
	id INTEGER NOT NULL, 
	name VARCHAR(80), 
	PRIMARY KEY (id), 
	UNIQUE (name)
);
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
CREATE TABLE feed (
	id INTEGER NOT NULL, 
	title VARCHAR(200), 
	url VARCHAR(200), 
	user_id INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (title), 
	UNIQUE (url), 
	FOREIGN KEY(user_id) REFERENCES user (id)
);
CREATE TABLE tagmap (
	tag_id INTEGER, 
	feed_id INTEGER, 
	FOREIGN KEY(tag_id) REFERENCES tag (id), 
	FOREIGN KEY(feed_id) REFERENCES feed (id)
);
CREATE TABLE entry (
	id INTEGER NOT NULL, 
	title VARCHAR(120), 
	description TEXT, 
	link VARCHAR(200), 
	pubdate DATETIME, 
	feed_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(feed_id) REFERENCES feed (id)
);
COMMIT;
