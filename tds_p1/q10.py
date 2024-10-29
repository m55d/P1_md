import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the users data
users_df = pd.read_csv('users.csv')

# Prepare data for regression
X = users_df[['public_repos']]  # Predictor variable
y = users_df['followers']        # Response variable

# Fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Get the slope (coefficient) of the regression
slope = model.coef_[0]

# Display the slope rounded to 3 decimal places
print(f'Regression slope of followers on public repositories: {slope:.3f}')
