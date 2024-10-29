import pandas as pd

# Load the repositories data
repos_df = pd.read_csv('repositories.csv')

# Check for missing values in the 'language' and 'stargazers_count' columns and drop them
repos_df = repos_df.dropna(subset=['language', 'stargazers_count'])

# Group by programming language and calculate the average number of stars
average_stars = repos_df.groupby('language')['stargazers_count'].mean()

# Identify the language with the highest average stars
highest_avg_language = average_stars.idxmax()
highest_avg_stars = average_stars.max()

print(f'The programming language with the highest average number of stars per repository is: {highest_avg_language} with an average of {highest_avg_stars:.2f} stars.')
