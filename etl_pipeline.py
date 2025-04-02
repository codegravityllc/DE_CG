

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


