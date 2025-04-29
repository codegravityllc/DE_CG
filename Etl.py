import pandas as pd
import psycopg2
import re

conn = psycopg2.connect(
    host="localhost",
    port = 5432,
    database="CGDB",
    user="postgres",
    password="Test123")

data = pd.read_csv(r'C:\Users\Pravasis Dhakal\Desktop\project code gravity\DataEngineer.csv')

df=data

# Function to clean and transform salary data
def extract_salary(salary_str):
    match = re.findall(r'\$([\dK]+)-\$([\dK]+)', salary_str)
    if match:
        min_salary = int(match[0][0].replace('K', '')) * 1000
        max_salary = int(match[0][1].replace('K', '')) * 1000
        avg_salary = (min_salary + max_salary) // 2
        return min_salary, max_salary, avg_salary
    return None, None, None

# Apply transformation
df[['salary_min', 'salary_max', 'salary_avg']] = df['Salary Estimate'].apply(
    lambda x: pd.Series(extract_salary(str(x)))
)

# Remove unnecessary columns
df_cleaned = df[['Job Title', 'salary_min', 'salary_max', 'salary_avg',
                 'Job Description', 'Rating', 'Company Name', 'Location',
                 'Headquarters', 'Size', 'Founded', 'Type of ownership',
                 'Industry', 'Sector', 'Revenue']]

# Rename columns for database insertion
df_cleaned.columns = ['job_title', 'salary_min', 'salary_max', 'salary_avg',
                      'job_description', 'rating', 'company_name', 'location',
                      'headquarters', 'size', 'founded', 'type_of_ownership',
                      'industry', 'sector', 'revenue']


# Function to insert data into PostgreSQL
def insert_into_db(df):
    try:
        conn = psycopg2.connect(
            dbname= "CGDB" , user= "postgres", password= "Test123", host= "localhost", port= "5432"
        )


        cursor = conn.cursor()

        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO job_listings (job_title, salary_min, salary_max, salary_avg,
                                         job_description, rating, company_name, location,
                                         headquarters, size, founded, type_of_ownership,
                                         industry, sector, revenue)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, tuple(row))

        conn.commit()
        cursor.close()
        conn.close()
        print("Data successfully inserted into PostgreSQL.")

    except Exception as e:
        print("Error inserting data:", e)

# Run the ETL process
insert_into_db(df_cleaned)