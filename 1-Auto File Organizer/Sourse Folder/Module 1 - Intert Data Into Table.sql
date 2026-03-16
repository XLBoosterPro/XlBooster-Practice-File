select * from student

alter table student
rename column fee to fees

insert into student (stu_id, stu_name, age, gender, course, fees)
	values (1, 'Sachin Singh', 21, 'Male', 'Advance Excel', 4500);
	
	
insert into student (stu_id, stu_name, age, gender, course, fees)
	values (2, 'Jay Jadhav', 20, 'Male', 'Power BI', 9500);
	
	
insert into student values (3, 'Ramesh Shinde', 19, 'Male', 'Power BI', 9500);
										
						
insert into student values (4, 'Aakash Singh', 23, 'Male', 'SQL', 8500),
					 (5, 'Sangeeta Jadhav', 22, 'Female', 'Advance Excel', 4500),
					 (6, 'Aneeta Kale', 24, 'Female', 'Advance Excel', 4500);

					

