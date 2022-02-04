show databases;
create database pythonDB;
use pythonDB;
show tables;
create table empinfo(eid int, ename varchar(20), sal float);
desc empinfo;
insert into empinfo values(1,'Shital',450000.50);
select * from empinfo;
select * from empdata;
select * from crudapp_employee;
select * from home_contact;


select * from taskmanager_tasks;
select * from taskmanager_signup;

select Username from taskmanager_signup;
select Password from taskmanager_signup;
delete from taskmanager_signup where First_Name = 'abc'
drop table taskmanager_signup
create table taskmanager_signup(Id integer AUTO_INCREMENT NOT NULL PRIMARY KEY, Username varchar(100) NOT NULL, First_Name varchar(100) NOT NULL, Last_Name varchar(100) NOT NULL,
Email varchar(100) NOT NULL, Password varchar(100) NOT NULL, Confirm_Password varchar(100) NOT NULL)
create view demo_vw as select username from taskmanager_signup where username = 'user1'
SELECT * FROM  demo_vw  


ALTER TABLE empinfo ADD DOB date 
ALTER TABLE empinfo DROP COLUMN DOB
ALTER TABLE empinfo RENAME TO empdata
ALTER TABLE empdata DROP COLUMN DOB

/* Class 03/02/2022  Practice*/

create table student(sid int, sname varchar(20), percentage float)
insert into student values(4,'Shilpa', 96.50)

select * from student
select sname from student
SELECT DISTINCT sname FROM student
SELECT COUNT(DISTINCT sname) FROM student 
SELECT * FROM student WHERE sname='Shilpa' AND percentage=96.50
SELECT * FROM student WHERE sname='Shilpa' OR sname='Shubham'
SELECT * FROM student WHERE NOT sname='Shilpa'
SELECT * FROM student WHERE sname IN ('Shilpa', 'Shubham', 'Rohit')
SELECT * FROM student WHERE sname NOT IN ('Shilpa', 'Shubham', 'Rohit')
SELECT * FROM student WHERE percentage BETWEEN 90 AND 100
SELECT * FROM student WHERE percentage NOT BETWEEN 90 AND 100 
SELECT * FROM student WHERE sname LIKE 's%'
SELECT * FROM student WHERE sname LIKE '%a'
SELECT * FROM student WHERE sname LIKE '%i%'
SELECT * FROM student WHERE sname LIKE '___l%'
SELECT * FROM student WHERE sname LIKE 's__%'
SELECT * FROM student WHERE sname LIKE 's%a'
SELECT * FROM student WHERE sname NOT LIKE 'a%'
SELECT * FROM student LIMIT 3
SELECT * FROM student WHERE sname='Shilpa' LIMIT 3
SELECT * FROM student WHERE sname is null
SELECT * FROM student WHERE sname is not null
SELECT * FROM student ORDER BY sid
SELECT * FROM student ORDER BY sid desc
SELECT * FROM student ORDER BY sid desc, sname asc
SELECT COUNT(sid), sname FROM student GROUP BY sname 
SELECT COUNT(sid), sname FROM student GROUP BY sname HAVING COUNT(sid) > 1   
SELECT sid,sname FROM student GROUP BY sname WITH ROLLUP
select sname as student_name from student

insert into student values(5,'Vitthal', 97.50)
INSERT INTO student (sname) VALUES ('Ishiqa')
INSERT INTO student (sid, sname) VALUES (6,'Samiksha')
INSERT INTO student (sname) VALUES ('Swati'), ('Shakti')
INSERT IGNORE INTO student (sid, sname, percentage ) VALUES (7, 'Ram', 75)
INSERT INTO student (sid, sname, percentage ) SELECT eid, ename, sal FROM empdata

UPDATE student SET sname = 'Alfred Schmidt' WHERE sid = 1;
UPDATE student SET sname = 'John', percentage=70.00 WHERE sid = 1;

DELETE FROM student WHERE sname='John';
DELETE FROM student WHERE sname='Shubham' and percentage = 75;

	

CREATE VIEW s_view AS SELECT sname FROM student WHERE sid = 1; 
select * from s_view;
drop view s_view
























