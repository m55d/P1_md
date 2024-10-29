# import pandas as pd

# # Load the users data
# users_df = pd.read_csv('users.csv')

# # Convert 'following' column to numeric and drop NaN values
# users_df['following'] = pd.to_numeric(users_df['following'], errors='coerce')

# # Check counts of hireable and non-hireable users
# hireable_count = users_df[users_df['hireable'] == True].shape[0]
# non_hireable_count = users_df[users_df['hireable'] == False].shape[0]
# print(f'Hireable users: {hireable_count}, Non-hireable users: {non_hireable_count}')

# # Calculate average following for hireable users
# average_hireable_following = users_df[users_df['hireable'] == True]['following'].dropna().mean()

# # Calculate average following for non-hireable users
# average_non_hireable_following = users_df[users_df['hireable'] == False]['following'].dropna().mean()

# # Calculate the difference
# difference = average_hireable_following - average_non_hireable_following

# # Display the result rounded to 3 decimal places
# print(f'Difference in average following (hireable - non-hireable): {difference:.3f}')


import pandas as pd

# Load the user data
users_df = pd.read_csv('users.csv')

# Filter the DataFrame based on hireable status and calculate averages
hireable_following_avg = users_df[users_df['hireable'] == True]['following'].mean()
non_hireable_following_avg = users_df[users_df['hireable'] == False]['following'].mean()

# Calculate the difference
difference = hireable_following_avg - non_hireable_following_avg

# Print the result to 3 decimal places
print(f"{difference:.3f}")

