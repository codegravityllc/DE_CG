#DataAnalysis AdzunaAPI

SELECT * FROM job_listings;

#Do Basic Analysis
SELECT job_title, company_name, salary_avg
FROM job_listings
ORDER BY salary_avg DESC
LIMIT 10;

#Count_jobs_by_Locations
SELECT location, COUNT(*) AS job_count
FROM job_listings
GROUP BY location
ORDER BY job_count DESC;

#UpdatedATA
SELECT job_title, company_name, location
FROM job_listings
WHERE job_description ILIKE '%python%';
UPDATE job_listings
SET rating = 0
WHERE rating IS NULL;
DELETE FROM job_listings
WHERE salary_avg < 20000;


#Create Indxes(creating viwe for Reporting)
CREATE INDEX idx_location ON job_listings(location);
CREATE INDEX idx_company_name ON job_listings(company_name);

#view for reporting
CREATE VIEW high_paying_jobs AS
SELECT job_title, company_name, salary_avg
FROM job_listings
WHERE salary_avg > 100000;