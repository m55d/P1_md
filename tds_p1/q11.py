import pandas as pd

# Load the repositories data
repos_df = pd.read_csv('repositories.csv')

# Check if 'has_projects' and 'has_wiki' are present and convert them to binary
repos_df['has_projects'] = repos_df['has_projects'].map({True: 1, False: 0})
repos_df['has_wiki'] = repos_df['has_wiki'].map({True: 1, False: 0})

# Drop rows with NaN values in either 'has_projects' or 'has_wiki'
cleaned_repos_df = repos_df.dropna(subset=['has_projects', 'has_wiki'])

# Calculate the correlation
correlation = cleaned_repos_df['has_projects'].corr(cleaned_repos_df['has_wiki'])

# Display the correlation rounded to 3 decimal places
print(f'Correlation between projects enabled and wiki enabled: {correlation:.3f}')
