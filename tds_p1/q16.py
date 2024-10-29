import pandas as pd

# Load the users data
users_df = pd.read_csv('users.csv')

# Drop rows where the 'name' column is NaN
users_df = users_df[users_df['name'].notna()]

# Extract surnames from names (last word after splitting and stripping whitespace)
users_df['surname'] = users_df['name'].apply(lambda x: x.strip().split()[-1] if isinstance(x, str) and x.strip() else None)

# Drop rows where the 'surname' is NaN after extraction
users_df = users_df[users_df['surname'].notna()]

# Count the occurrences of each surname
surname_counts = users_df['surname'].value_counts()

# Get the most common surname(s)
if not surname_counts.empty:
    most_common_surnames = surname_counts[surname_counts == surname_counts.max()].index.tolist()
    most_common_count = surname_counts.max()
    
    print(f'Most common surname(s): {", ".join(most_common_surnames)}')
    print(f'Number of users with the most common surname: {most_common_count}')
else:
    print("No valid surnames found.")
