_HiStOrY_V2_
exit()
exit
eixt
exit
--creation
.help
CREATE TABLE author (
author_id INTEGER NOT NULL PRIMARY KEY,
first_name VARCHAR,
last_name VARCHAR
);
.tables
-- querying
SELECT * FROM author;
INSERT INTO author(first_name, last_name) VALUES ('Isaac', 'Asimov');
INSERT INTO author(first_name, last_name) VALUES ('Pearl', 'Buck');
SELECT * FROM author;
INSERT INTO author(first_name, last_name) VALUES ('Tim ', 'Clancy');
SELECT * FROM author;
UPDATE author SET first_name='Tom' WHERE author_id=3;
SELECT * FROM author;
SELECT * FROM author;
SELECT FIRST_NAME FROM author;
INSERT INTO author(first_name, last_name) VALUES ('Tim ', 'Clancy');
DELETE FROM author WHERE last_name='Clancy';
SELECT FIRST_NAME FROM author;
SELECT * FROM author;
-- Relations
create table book (
book_id integer not null primary key,
title varchar,
author_id integer references author
);
.tables
insert into book (title, author_id) values ('Foundation','1');
SELECT * FROM book;
insert into book (title, author_id) values ('The Good Earth','2');
SELECT * FROM book;
select
a.first_name || ' ' || a.last_name as author_name
,
b.title as book_title
from author a
join book b on b.author_id = a.author_id
order by a.last_name asc;
history
;
.exit