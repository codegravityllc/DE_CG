import requests
import pandas as pd
import psycopg2

# Replace these with your real credentials
APP_ID = '3f681fcf'
APP_KEY = 'cc6729428ba9dc678076f700ff20617b'

# Adzuna API endpoint and parameters
API_URL = "https://api.adzuna.com/v1/api/jobs/us/search/1"
params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "results_per_page": 50,
    "what": "Data Engineer",
    "content-type": "application/json"
}


# Function to extract job data from Adzuna API
def extract_from_api():
    response = requests.get(API_URL, params=params)
    if response.status_code != 200:
        raise Exception(f"API Error {response.status_code}: {response.text}")

    results = response.json().get("results", [])
    df = pd.json_normalize(results)

    # Transform fields to match database schema
    df['job_title'] = df['title']
    df['company_name'] = df['company.display_name']
    df['location'] = df['location.display_name']
    df['salary_min'] = df['salary_min'].fillna(0).astype(int)
    df['salary_max'] = df['salary_max'].fillna(0).astype(int)
    df['salary_avg'] = (df['salary_min'] + df['salary_max']) // 2
    df['job_description'] = df['description']

    # Fill placeholders for missing fields
    df['rating'] = None
    df['headquarters'] = None
    df['size'] = None
    df['founded'] = None
    df['type_of_ownership'] = None
    df['industry'] = None
    df['sector'] = None
    df['revenue'] = None

    # Select final columns for DB
    df_cleaned = df[['job_title', 'salary_min', 'salary_max', 'salary_avg',
                     'job_description', 'rating', 'company_name', 'location',
                     'headquarters', 'size', 'founded', 'type_of_ownership',
                     'industry', 'sector', 'revenue']]

    return df_cleaned


# Function to insert DataFrame into PostgreSQL
def insert_into_db(df):
    try:
        conn = psycopg2.connect(
            dbname="CGDB", user="postgres",
            password="Test123", host="localhost", port="5432"
        )
        cursor = conn.cursor()

        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO job_listings (
                    job_title, salary_min, salary_max, salary_avg,
                    job_description, rating, company_name, location,
                    headquarters, size, founded, type_of_ownership,
                    industry, sector, revenue
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, tuple(row))

        conn.commit()
        cursor.close()
        conn.close()
        print("Data successfully inserted into PostgreSQL.")
    except Exception as e:
        print("Error inserting data:", e)


# Run the ETL process
if __name__ == "__main__":
    df_jobs = extract_from_api()
    insert_into_db(df_jobs)