import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the user data
users_df = pd.read_csv('users.csv')

# Check for NaN values in bio and followers
print(f'Number of NaN values in bio: {users_df["bio"].isna().sum()}')
print(f'Number of NaN values in followers: {users_df["followers"].isna().sum()}')

# Filter out users without bios
users_df = users_df[users_df['bio'].notna()]

# Calculate the length of each bio in words
users_df['bio_word_count'] = users_df['bio'].str.split().str.len()

# Remove users with no followers or where bio_word_count is NaN
filtered_users = users_df[(users_df['followers'].notna()) & (users_df['bio_word_count'].notna())]

# Print statistics of the filtered data
print(filtered_users[['bio_word_count', 'followers']].describe())

# Visualize the relationship
plt.scatter(filtered_users['bio_word_count'], filtered_users['followers'])
plt.xlabel('Bio Word Count')
plt.ylabel('Number of Followers')
plt.title('Followers vs. Bio Word Count')
plt.show()

# Remove outliers based on followers
filtered_users = filtered_users[filtered_users['followers'] < filtered_users['followers'].quantile(0.95)]

# Prepare the features and target variable
X = filtered_users[['bio_word_count']]
y = filtered_users['followers']

# Fit the regression model
model = LinearRegression()
model.fit(X, y)

# Get the slope (coefficient)
slope = model.coef_[0]

# Print the slope rounded to 3 decimal places
print(f'Regression slope of followers on bio word count: {slope:.3f}')

# Calculate the correlation
correlation = filtered_users['bio_word_count'].corr(filtered_users['followers'])
print(f'Correlation between bio word count and followers: {correlation:.3f}')
