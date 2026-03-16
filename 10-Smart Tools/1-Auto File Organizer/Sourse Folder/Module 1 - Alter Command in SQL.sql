create table student
(
	stu_id int primary key,
	stu_name varchar(50) not null,
	age int not null,
	gender varchar(10),
	course varchar(30),
	fee numeric
);

select * from student

alter table student
rename column fee to fees

alter table student
Add column Balance_Fees numeric

alter table student
drop column balance_fees

alter table student
alter column course type varchar(30)

alter table student1
rename to student

drop table student



