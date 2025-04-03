import requests
import pandas as pd

# Replace these with your real credentials
APP_ID = '3f681fcf'
APP_KEY = 'cc6729428ba9dc678076f700ff20617b'

# Base API endpoint
url = "https://api.adzuna.com/v1/api/jobs/us/search/1"

# API parameters
params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "results_per_page": 50,
    "what": "Data Engineer",
    "content-type": "application/json"
}

# Make the request
response = requests.get(url, params=params)

# Check status
if response.status_code == 200:
    data = response.json()
    results = data.get('results', [])
    df = pd.json_normalize(results)
    print(df[['title', 'company.display_name', 'location.display_name', 'salary_min', 'salary_max']].head())
else:
    print("Error:", response.status_code, response.text)

    df['job_title'] = df['title']
    df['company_name'] = df['company.display_name']
    df['location'] = df['location.display_name']
    df['salary_min'] = df['salary_min'].fillna(0).astype(int)
    df['salary_max'] = df['salary_max'].fillna(0).astype(int)
    df['salary_avg'] = (df['salary_min'] + df['salary_max']) // 2
    df['job_description'] = df['description']

    # Fill in dummy/defaults for fields not provided by Adzuna
    df['rating'] = None
    df['headquarters'] = None
    df['size'] = None
    df['founded'] = None
    df['type_of_ownership'] = None
    df['industry'] = None
    df['sector'] = None
    df['revenue'] = None

    # Keep only relevant columns
    df_cleaned = df[['job_title', 'salary_min', 'salary_max', 'salary_avg',
                     'job_description', 'rating', 'company_name', 'location',
                     'headquarters', 'size', 'founded', 'type_of_ownership',
                     'industry', 'sector', 'revenue']]

