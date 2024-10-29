# import pandas as pd

# # Load the users data
# users_df = pd.read_csv('users.csv')

# # Load the repositories data
# repos_df = pd.read_csv('repositories.csv')

# # Convert the 'created_at' column to datetime
# users_df['created_at'] = pd.to_datetime(users_df['created_at'])

# # Filter users who joined after January 1, 2021
# filtered_users = users_df[users_df['created_at'] > '2021-01-01']

# # Check the number of filtered users
# print(f'Number of users who joined after 2020: {len(filtered_users)}')

# # Merge the filtered users with their repositories
# merged_df = repos_df[repos_df['login'].isin(filtered_users['login'])]

# # Count the number of repositories for each programming language
# language_counts = merged_df['language'].value_counts()

# # Check if there are enough languages to find the second most popular
# if len(language_counts) >= 2:
#     second_most_popular_language = language_counts.index[1]  # Get the second most popular
#     second_most_count = language_counts.iloc[1]  # Get the count of the second most popular
#     print(f'The second most popular programming language among users who joined after 2020 is: {second_most_popular_language} with {second_most_count} repositories.')
# else:
#     print('Not enough programming languages found for users who joined after 2020.')


import pandas as pd

# Load the users data
users_df = pd.read_csv('users.csv')

# Load the repositories data
repos_df = pd.read_csv('repositories.csv')

# Convert the 'created_at' column to datetime
users_df['created_at'] = pd.to_datetime(users_df['created_at'])

# Filter users who joined after January 1, 2021
filtered_users = users_df[users_df['created_at'] > '2021-01-01']

# Check the number of filtered users
print(f'Number of users who joined after 2020: {len(filtered_users)}')

# Merge the filtered users with their repositories
merged_df = repos_df[repos_df['login'].isin(filtered_users['login'])]

# Check for missing values in the 'language' column and drop them
merged_df = merged_df.dropna(subset=['language'])

# Count the number of repositories for each programming language
language_counts = merged_df['language'].value_counts()

# Check if there are enough languages to find the second most popular
if len(language_counts) >= 2:
    second_most_popular_language = language_counts.index[1]  # Get the second most popular
    second_most_count = language_counts.iloc[1]  # Get the count of the second most popular
    print(f'The second most popular programming language among users who joined after 2020 is: {second_most_popular_language} with {second_most_count} repositories.')
else:
    print('Not enough programming languages found for users who joined after 2020.')
