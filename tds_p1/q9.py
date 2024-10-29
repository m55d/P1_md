# import pandas as pd

# # Load the users data
# users_df = pd.read_csv('users.csv')

# # Ensure the data types are numeric
# users_df['followers'] = pd.to_numeric(users_df['followers'], errors='coerce')
# users_df['public_repos'] = pd.to_numeric(users_df['public_repos'], errors='coerce')

# # Check for NaN values in followers and public_repos after conversion
# print("Number of NaN values in followers:", users_df['followers'].isna().sum())
# print("Number of NaN values in public_repos:", users_df['public_repos'].isna().sum())

# # Drop rows with NaN values in either followers or public_repos
# cleaned_users_df = users_df.dropna(subset=['followers', 'public_repos'])

# # Check for constant values
# if cleaned_users_df['followers'].nunique() < 2:
#     print("The 'followers' column has constant values. Cannot compute correlation.")
# elif cleaned_users_df['public_repos'].nunique() < 2:
#     print("The 'public_repos' column has constant values. Cannot compute correlation.")
# else:
#     # Calculate correlation between followers and public repositories
#     correlation = cleaned_users_df['followers'].corr(cleaned_users_df['public_repos'])

#     # Display the correlation rounded to 3 decimal places
#     print(f'Correlation between followers and public repositories: {correlation:.3f}')





import csv
import numpy as np

# Lists to store the followers and public repos of users from Delhi
followers = []
public_repos = []

# Open the users.csv file and read data
with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Filter for users in Delhi
        location = row.get('location', '').strip().lower()
        if "delhi" in location:
            # Get followers and public repositories values
            try:
                followers_count = int(row['followers'])
                public_repos_count = int(row['public_repos'])
                
                # Append the valid values to the lists
                followers.append(followers_count)
                public_repos.append(public_repos_count)
            except ValueError:
                # Skip rows with invalid numerical values
                continue

# Ensure there is data to compute correlation
if len(followers) > 1 and len(public_repos) > 1:
    # Compute Pearson correlation coefficient
    correlation_matrix = np.corrcoef(followers, public_repos)
    correlation = correlation_matrix[0, 1]
    # Output correlation rounded to 3 decimal places
    print(f"{correlation:.3f}")
else:
    print("Insufficient data for correlation calculation.")
