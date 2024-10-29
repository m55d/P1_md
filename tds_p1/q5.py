import pandas as pd

# Load the repositories data
repos_df = pd.read_csv('repositories.csv')

# Check the first few rows to understand the structure
print("Original DataFrame:")
print(repos_df.head())

# Count the number of repositories for each programming language
language_counts = repos_df['language'].value_counts()

# Check if language_counts is empty before attempting to get the most popular language
if not language_counts.empty:
    most_popular_language = language_counts.idxmax()
    most_popular_count = language_counts.max()
    print(f'The most popular programming language is: {most_popular_language} with {most_popular_count} repositories.')
else:
    print('No valid programming language entries found.')
