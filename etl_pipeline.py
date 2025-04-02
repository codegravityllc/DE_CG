import pandas as pd
import psycopg2
import re

conn = psycopg2.connect(
    host="localhost",
    port = 5432,
    database="Cgdb",
    user="postgres",
    password="Password")

data = pd.read_csv(r'/Users/binita/Desktop\DataEngineer (1).csv')

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







