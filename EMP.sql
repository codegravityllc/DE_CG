CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2)
);

DESCRIBE employees;

SHOW PROCESSLIST;

SELECT table_schema AS database_name, 
       ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS size_in_MB
FROM information_schema.tables 
GROUP BY table_schema;

SHOW INDEX FROM employees;







