CREATE TABLE job_listings (
job_id SERIAL PRIMARY KEY,
job_title TEXT,
salary_min INTEGER,
salary_max INTEGER,
salary_avg INTEGER,
job_description TEXT,
rating FLOAT,
company_name TEXT,
location TEXT,
headquarters TEXT,
size TEXT,
founded INTEGER,
type_of_ownership TEXT,
industry TEXT,
sector TEXT,
revenue TEXT
);
 select *from job_listings;

SELECT industry, AVG(salary_avg) AS avg_salary
FROM job_listings
GROUP BY industry
ORDER BY avg_salary DESC

