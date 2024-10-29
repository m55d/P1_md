import pandas as pd

# Load the users data
repos_df = pd.read_csv('repositories.csv')

# Convert the 'created_at' column to datetime
repos_df['created_at'] = pd.to_datetime(repos_df['created_at'])

# Filter for repositories created on weekends (Saturday and Sunday)
repos_df['weekday'] = repos_df['created_at'].dt.weekday
weekend_repos = repos_df[repos_df['weekday'].isin([5, 6])]  # 5=Saturday, 6=Sunday

# Count repositories created by each user on weekends
weekend_counts = weekend_repos['login'].value_counts()

# Get the top 5 users who created the most repositories
top_users = weekend_counts.head(5).index.tolist()
print("Top 5 users who created the most repositories on weekends:", ", ".join(top_users))
