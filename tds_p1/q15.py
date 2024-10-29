import pandas as pd
# Load the users data
users_df = pd.read_csv('users.csv')

# Calculate the fraction of users with email addresses
total_users = len(users_df)
hireable_users_with_email = len(users_df[users_df['hireable'] == True & users_df['email'].notna()])
non_hireable_users_with_email = len(users_df[users_df['hireable'] == False & users_df['email'].notna()])

# Calculate fractions
fraction_hireable = hireable_users_with_email / len(users_df[users_df['hireable'] == True]) if len(users_df[users_df['hireable'] == True]) > 0 else 0
fraction_non_hireable = non_hireable_users_with_email / len(users_df[users_df['hireable'] == False]) if len(users_df[users_df['hireable'] == False]) > 0 else 0

# Calculate the difference
email_difference = fraction_hireable - fraction_non_hireable
print(f'Email difference between hireable and non-hireable users: {email_difference:.3f}')
