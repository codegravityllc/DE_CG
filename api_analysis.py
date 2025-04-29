import requests
import pandas as pd

# Step 1: Set your Adzuna API credentials
APP_ID = '3f681fcf'
APP_KEY = 'cc6729428ba9dc678076f700ff20617b'

# Step 2: Define Adzuna API endpoint and parameters
API_URL = "https://api.adzuna.com/v1/api/jobs/us/search/1"
params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "results_per_page": 50,
    "what": "Data Engineer",  # Or any other job title
    "content-type": "application/json"
}


# Step 3: Extract job data from Adzuna API
def extract_from_api():
    response = requests.get(API_URL, params=params)
    if response.status_code != 200:
        raise Exception(f"API Error {response.status_code}: {response.text}")

    data = response.json().get("results", [])
    df = pd.json_normalize(data)
    return df


# Step 4: Load the data
df = extract_from_api()

# Step 5: Display first few rows
print(df.head())

# Step 6: Analyze top companies hiring
top_companies = df['company.display_name'].value_counts().head(10)
print("Top hiring companies:\n", top_companies)

# Step 7: Analyze average and top salaries
df['salary_mean'] = (df['salary_min'] + df['salary_max']) / 2
average_salary = df['salary_mean'].mean()
top_salaries = df[['company.display_name', 'salary_mean']].sort_values(by='salary_mean', ascending=False).head(10)

print(f"\nAverage salary for Data Engineer roles: ${average_salary:,.2f}")
print("\nTop 10 companies offering highest salaries:\n", top_salaries)

# Step 8: Analyze job locations
top_locations = df['location.area'].apply(lambda x: x[-1] if isinstance(x, list) else None).value_counts().head(10)
print("\nTop job locations:\n", top_locations)

# Step 9: Skills analysis (if skills field available)
# If 'description' field exists, find common keywords
from collections import Counter
import re

# Combine all descriptions
all_descriptions = " ".join(df['description'].dropna())

# Extract skills/keywords (basic example)
keywords = re.findall(r'\b(Python|SQL|AWS|Azure|Spark|Hadoop|Kafka|ETL|Tableau|Snowflake|Power BI|Pandas|Docker|Airflow)\b', all_descriptions, flags=re.IGNORECASE)
keyword_counts = Counter([k.lower() for k in keywords])

print("\nTop mentioned technologies/skills:\n", keyword_counts.most_common(10))


# Step 3: Extract job data from Adzuna API
def extract_from_api():
    response = requests.get(API_URL, params=params)
    if response.status_code != 200:
        raise Exception(f"API Error {response.status_code}: {response.text}")

    data = response.json().get("results", [])
    df = pd.json_normalize(data)
    return df


# Step 4: Load the data
df = extract_from_api()

# Step 5: Display first few rows
print(df.head())

import matplotlib.pyplot as plt

# Top Companies Plot
top_companies.plot(kind='barh', figsize=(10,6), title="Top Hiring Companies for Data Engineers")
plt.gca().invert_yaxis()
plt.show()

# Top Locations Plot
top_locations.plot(kind='barh', figsize=(10,6), title="Top Job Locations for Data Engineers")
plt.gca().invert_yaxis()
plt.show()