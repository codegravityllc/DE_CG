CREATE TABLE COMPANY (
    id INT AUTO_INCREMENT PRIMARY KEY,
    job_title VARCHAR(255),
    salary_estimate VARCHAR(255),
    job_description TEXT,
    rating DECIMAL(3, 2),
    company_name VARCHAR(255),
    location VARCHAR(255),
    headquarters VARCHAR(255),
    size VARCHAR(50),
    founded INT,
    type_of_ownership VARCHAR(50),
    industry VARCHAR(255),
    sector VARCHAR(255),
    revenue VARCHAR(50),
    competitors VARCHAR(255),
    easy_apply INT,

    INDEX idx_company_name (company_name)
);
