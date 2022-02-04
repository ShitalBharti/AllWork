SELECT * FROM student;

SELECT * FROM student group by sname, srollno, sbranch having count(*) >1; 

create table student_rd like student;
	
SELECT * FROM student_rd;    

INSERT INTO STUDENT_rd SELECT * FROM student group by sname, srollno, sbranch having count(*) >1; 

DELETE from student a where a.sname in(select * from (SELECT b.sname FROM student b group by b.sname, b.srollno, b.sbranch having count(*) >1) x); 

INSERT INTO student SELECT * FROM student_rd;