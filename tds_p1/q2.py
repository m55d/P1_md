import pandas as pd

# Load the users.csv file
users_df = pd.read_csv('users.csv')

# Convert 'created_at' column to datetime format if it isn't already
users_df['created_at'] = pd.to_datetime(users_df['created_at'])

# Sort users by 'created_at' in ascending order and select the top 5
earliest_users = users_df.sort_values(by='created_at').head(5)

# Extract the 'login' column as a list and join them with commas
earliest_user_logins = ', '.join(earliest_users['login'].tolist())
print("5 earliest registered users:", earliest_user_logins)











# import csv
# from datetime import datetime

# Define the list to store users from Delhi
# users_in_toronto = []

# # Read the CSV file with UTF-8 encoding
# with open('users.csv', 'r', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         location = row['location'].strip().lower()
#         # Check if the user is from Delhi
#         if 'delhi' in location:
#             users_in_toronto.append({
#                 'login': row['login'],
#                 'created_at': datetime.strptime(row['created_at'], '%Y-%m-%dT%H:%M:%SZ')
#             })

# # Sort users based on created_at in ascending order
# sorted_users = sorted(users_in_toronto, key=lambda x: x['created_at'])

# # Extract the top 5 user logins
# top_5_earliest_logins = [user['login'] for user in sorted_users[:5]]

# # Print the result as a comma-separated list
# print(','.join(top_5_earliest_logins))
