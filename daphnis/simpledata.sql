PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE tag (
	id INTEGER NOT NULL, 
	name VARCHAR(80), 
	PRIMARY KEY (id), 
	UNIQUE (name)
);
INSERT INTO "tag" VALUES(1,'test-tag');
CREATE TABLE entry (
	id INTEGER NOT NULL, 
	title VARCHAR(120), 
	description TEXT, 
	link VARCHAR(200), 
	pubdate DATETIME, 
	PRIMARY KEY (id)
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
INSERT INTO "user" VALUES(1,'fixed','test@test.com','pbkdf2:sha1:1000$IpIDYJGd$68ab7b378452581d4cbf5ed1f5f6646a9a107335',NULL,NULL);
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
INSERT INTO "feed" VALUES(1,'test feed','http://www.google.com',1);
CREATE TABLE tagmap (
	tag_id INTEGER, 
	feed_id INTEGER, 
	FOREIGN KEY(tag_id) REFERENCES tag (id), 
	FOREIGN KEY(feed_id) REFERENCES feed (id)
);
INSERT INTO "tagmap" VALUES(1,1);
COMMIT;
