/* CREATE THE DATABASE */
CREATE DATABASE employee;
/* SELECT THE DATABASE */
USE employee;
/* CREATE THE TABLE */
CREATE TABLE employee_table(
    emp_id INTEGER not NULL,
    emp_name VARCHAR(255) not null,
    emp_age INTEGER not NULL,
    emp_salary INTEGER not NULL,
    emp_gender VARCHAR(1) not NULL,
    emp_department VARCHAR(25) not null,
    PRIMARY KEY(emp_id)
);
/* INSERT INTO TABLE */
INSERT INTO employee_table VALUES(
    1, 'Samuel',22, 135000, 'M', 'Technologies',
    2, 'Nathan',29, 265000, 'M', 'Operations',
    3, 'Sophia',23, 225000, 'F', 'Analytics',
    4, 'Sven', 335000,26, 'M', 'Technologies',
    5, 'Angelica',30, 225000, 'F', 'Human Resource'
);
/* VIEW DATA FROM TABLE */
SELECT * FROM employee_table

/* GET DISTINCT VALUES FROM A COLUMN, WHICH MEANS YOU ONLY GET THE VALUES WHICH ARE DIFFERENT*/
SELECT DISTINCT emp_gender FROM employee_table;

/* WHERE CLAUSE */
/*
This is used when you want to extract records which satisfy a condition
e.g:
Lets get the records of employee where we have all the female employee
*/
SELECT * FROM employee_table WHERE emp_gender='F'

/* AND OPERATOR */
/*
And Operator displays records if all the conditions sperated by AND are TRUE
e.g:
Get the records of employee where the age is less than 30 of an employee and is a Male
*/
SELECT * FROM employee_table WHERE emp_gender='M' AND emp_age<30;

/* OR OPERATOR */
/*
OR Operator displays records if one of the conditions is satisfied
e.g:
Get the list of employees from either departments, 'Analytics' OR 'Technologies'
*/
SELECT * FROM employee_table WHERE emp_department='Analytics' OR emp_department='Technologies';

/* NOT OPERATOR */
/*
NOT Operator displays the records if the condition is NOT TRUE
e.g:
Get the list of employees who are not in Operations
*/
SELECT * FROM employee_table WHERE NOT emp_department='Operations';

/* LIKE OPERATOR */
/*
Like operator is used to extract records where a particular pattern is present
Like operator is used in conjunction with wild card characters
and there are 2 wild clard character availabe, '%' -> Represents zero, one or multiple characters
and '_' -> Represents a single characters.

e.g:
Lets extract a record where we the pattern matches,
get employee names where 
*/
SELECT * FROM employee_table WHERE emp_name LIKE 'S%';

