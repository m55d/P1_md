import pandas as pd

# Load the users data
users_df = pd.read_csv('users.csv')

# Calculate leader_strength
users_df['leader_strength'] = users_df['followers'] / (1 + users_df['following'])

# Sort users by leader_strength in descending order
top_users = users_df.sort_values(by='leader_strength', ascending=False)

# Get the top 5 users
top_5_logins = top_users['login'].head(5)

# Convert to a comma-separated string
top_5_logins_str = ', '.join(top_5_logins)

print(f'The top 5 users in terms of leader_strength are: {top_5_logins_str}')
