
Drop table Entry; 
CREATE TABLE `Entry` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`entry`	TEXT NOT NULL,
	`concept`	TEXT NOT NULL,
    'date' TEXT NOT NULL,
    'moodId' INTEGER NOT NULL,
    FOREIGN KEY(`moodId`) REFERENCES `Mood`(`id`)

);

CREATE TABLE `Mood` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `mood`    TEXT NOT NULL
);


INSERT INTO `Entry` VALUES (null, "learned hard stuff today", "hard stuff", "12/12/2020", 1);
INSERT INTO `Entry` VALUES (null, "learned easy stuff today", "easy stuff", "1/1/2021", 2);
INSERT INTO `Mood` VALUES (null, '🤮');
INSERT INTO `Mood` VALUES (null, '💩')