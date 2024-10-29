# import pandas as pd

# # Load the users data
# users_df = pd.read_csv('users.csv')

# # Print the original DataFrame and unique values in 'company'
# print("Original DataFrame:")
# print(users_df.head())
# print("\nUnique company values before cleaning:")
# print(users_df['company'].unique())

# # Count NaN and empty string entries
# print(f"\nNumber of NaN entries: {users_df['company'].isna().sum()}")
# print(f"Number of empty string entries: {(users_df['company'] == '').sum()}")

# # Convert the 'company' column to strings
# users_df['company'] = users_df['company'].fillna('').astype(str)

# # Clean the company names: trim whitespace, remove leading '@', and convert to uppercase
# users_df['company'] = users_df['company'].str.strip().str.lstrip('@').str.upper()

# # Filter out empty strings in the 'company' column
# filtered_users = users_df[users_df['company'] != '']

# # Print the number of entries in the filtered DataFrame
# print(f'\nNumber of users after filtering: {len(filtered_users)}')

# # Count the number of developers per company
# company_counts = filtered_users['company'].value_counts()

# # Check if company_counts is empty before attempting to get the most common company
# if not company_counts.empty:
#     most_common_company = company_counts.idxmax()
#     most_common_count = company_counts.max()
#     print(f'The company with the majority of developers is: {most_common_company} with {most_common_count} developers.')
# else:
#     print('No valid company entries found.')




import csv
from collections import Counter

# Define the list to store company names
companies = []

# Read the CSV file with UTF-8 encoding
with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Get and clean up the company field (ignore empty values)
        company = row.get('company', '').strip()
        if company:
            companies.append(company)

# Count the occurrence of each company
company_counts = Counter(companies)

# Find the most common company
most_common_company = company_counts.most_common(1)

# Print the result
if most_common_company:
    print(most_common_company[0][0])
else:
    print("No company data found.")


