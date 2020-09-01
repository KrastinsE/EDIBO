#Intro in MySQL

mysql -h database-1.cxnurhwpmz0x.eu-central-1.rds.amazonaws.com -P 3000 -u u24 -p 




-----------------
CREATE TABLE MyTBL(column1 varchar(5));

SELECT * FROM MyTBL;

INSERT INTO MyTBL (column1) VALUES ("text1");

UPDATE MyTBL SET column2=2

INSERT INTO MyTBL (column1) VALUES ('text2');

INSERT INTO MyTBL (column1) VALUES ('text3';

UPDATE MyTBL SET column2=10;

UPDATE MyTBL SET COLUMN2=12 WHERE COLUMN1='text1'

ALTER TABLE MyTBL ADD column3 INT NOT NULL DEFAULT 100;
----
01.09.2020.
ALTER TABLE MyTBL_10 MODIFY column1 varchar(5) DEFAULT 'ABCD';

Iečekot lielo tabulu - DESCRIBE MyTBL_10;

Iečekot tabulas kolonnu saturu - SELECT * FROM MyTBL_10;

Kolonnu nosaukumu maiņa - UPDATE MyTBL_10 SET column1='ABCDE' WHERE column3=2;

Uzlikt vairākus PRIMARY KEY - ALTER TABLE MyTBL_10 DROP PRIMARY KEY, ADD PRIMARY KEY (column2, column3);

Izmainīt kolonnu vērtības - UPDATE MyTBL_10 SET column3=4 WHERE column2=255; (Trešo kolonnu pie skaitļa 255, sauksim par nr. 4)


