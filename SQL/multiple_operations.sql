CREATE DATABASE employee;
USE employee;
CREATE TABLE employee_table(
    id INTEGER not NULL,
    name VARCHAR(255) not null,
    salary INTEGER not NULL,
    gender VARCHAR(1) not NULL,
    department VARCHAR(25) not null,
    PRIMARY KEY(id)
);
INSERT INTO employee_table VALUES(
    1, 'Samuel', 135000, 'M', 'BPO',
    2, 'Nathan', 265000, 'M', 'Operations',
    3, 'David', 225000, 'M', 'Analytics',
    4, 'Sven', 335000, 'M', 'Technologies',
    5, 'Jack', 225000, 'M', 'Human Resource'
);
SELECT * FROM employee_table