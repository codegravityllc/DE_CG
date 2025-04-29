SELECT industry, AVG(salary_avg) AS avg_salary
FROM job_listings
GROUP BY industry
ORDER BY avg_salary DESC;