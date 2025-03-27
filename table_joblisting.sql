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