use pythonDB;

create table dummy(
emp_id int not null,
name varchar(45) not null,
phone_no varchar(40) not null,
technology varchar(40) not null,
salary varchar(40) not null,
start_date varchar(40)not null,
comments varchar(50) not null,
primary key(emp_id))

comment = "this table contains all the employee details";

alter table dummy rename to employee;

desc employee;

select * from employee;

start transaction;

insert into employee values
("001","aaaa","123456789","java","20000","2022-01-01","none"),
("002","bbbb","23456789","c","21000","2022-01-02","none"),
("003","cccc","3456789","c++","22000","2022-01-03","none"),
("004","dddd","456789","python","23000","2022-01-04","none");

select * from employee;

savepoint s1;

update employee set salary=25000 where emp_id="001";

savepoint s2;

delete e from employee as e where e.technology="java" and e.salary=(
select * from (select max(salary) from employee where technology="java"
order by salary desc) x);

delete e from employee as e where e.salary in(select * from (select salary from employee where salary>"20000")x);

