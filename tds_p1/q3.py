import pandas as pd

# Load the repositories.csv file
repos_df = pd.read_csv('repositories.csv')

# Check if 'license_name' column exists
if 'license_name' in repos_df.columns:
    # Filter out missing license names
    licenses = repos_df['license_name'].dropna()

    # Count occurrences of each license
    license_counts = licenses.value_counts()

    # Get the top 3 most popular licenses
    top_3_licenses = license_counts.head(3).index.tolist()

    # Print the result as a comma-separated list
    print("Top 3 most popular licenses:", ', '.join(top_3_licenses))
else:
    print("The 'license_name' column was not found in repositories.csv")
