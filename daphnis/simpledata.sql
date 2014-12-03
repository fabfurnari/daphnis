PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
INSERT INTO "tag" VALUES(1,'uncategorized');
INSERT INTO "tag" VALUES(2,'sport');
INSERT INTO "tag" VALUES(3,'cinema');

INSERT INTO "user" VALUES(1,'fixed','test@test.com','pbkdf2:sha1:1000$IpIDYJGd$68ab7b378452581d4cbf5ed1f5f6646a9a107335',NULL,NULL);

INSERT INTO "feed" VALUES(1,'Test feed','http://www.feedforall.com/sample.xml',1);
INSERT INTO "feed" VALUES(2,'Another test','http://www.feedforall.com/sample-feed.xml',1);
INSERT INTO "feed" VALUES(3,'Invalid feed','http://www.none.com',1);

INSERT INTO "tagmap" VALUES(1,1);
INSERT INTO "tagmap" VALUES(2,2);
INSERT INTO "tagmap" VALUES(2,3);
INSERT INTO "tagmap" VALUES(3,3);

COMMIT;
