import pandas as pd

# Load the CSV file
users_df = pd.read_csv('users.csv')

# Sort by 'followers' column in descending order
top_users = users_df.sort_values(by='followers', ascending=False).head(5)

# Extract the 'login' column as a list and join them with commas
top_user_logins = ', '.join(top_users['login'].tolist())
print("Top 5 users by followers:", top_user_logins)



# import csv

# # Define the list to store users from Toronto
# users_in_toronto = []

# # Read the CSV file with UTF-8 encoding
# with open('users.csv', 'r', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         location = row['location'].strip().lower()
#         # Check if the user is from Toronto
#         if 'toronto' in location:
#             users_in_toronto.append({
#                 'login': row['login'],
#                 'followers': int(row['followers'])
#             })

# # Sort users based on followers in descending order
# top_users = sorted(users_in_toronto, key=lambda x: x['followers'], reverse=True)

# # Extract the top 5 user logins
# top_5_logins = [user['login'] for user in top_users[:5]]

# # Print the result as a comma-separated list
# print(','.join(top_5_logins))
