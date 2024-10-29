from config import GITHUB_TOKEN
import requests
import pandas as pd
import time

headers = {'Authorization': f'token {GITHUB_TOKEN}'}

def fetch_users():
    users = []
    page = 1
    print("Fetching users...") 
    while True:
       
        url = f"https://api.github.com/search/users?q=location:Toronto+followers:>100&page={page}"
        response = requests.get(url, headers=headers)
        data = response.json()
        
        # Break if there are no more users
        if 'items' not in data or not data['items']:
            break
        
        for user in data['items']:
            # Fetch detailed user data
            user_url = f"https://api.github.com/users/{user['login']}"
            user_response = requests.get(user_url, headers=headers)
            user_data = user_response.json()
            
            # Clean up and process each field
            company = user_data.get('company', '')
            if company:
                company = company.strip('@ ').upper()  # Clean up company names
            
            users.append({
                'login': user_data['login'],
                'name': user_data.get('name', ''),
                'company': company,
                'location': user_data.get('location', 'Toronto'),
                'email': user_data.get('email', ''),
                'hireable': user_data.get('hireable', ''),
                'bio': user_data.get('bio', ''),
                'public_repos': user_data.get('public_repos', ''),
                'followers': user_data.get('followers', ''),
                'following': user_data.get('following', ''),
                'created_at': user_data.get('created_at', '')
            })
            time.sleep(0.5)  # Pause to avoid hitting rate limits
        
        print(f"Fetched page {page}...")  # Progress update
        page += 1  # Fetch next page

    # Save to users.csv
    users_df = pd.DataFrame(users)
    users_df.to_csv('users.csv', index=False)
    print("User data saved to users.csv")  # Completion message

# Run the function to fetch and save users
fetch_users()
def fetch_repositories(users):
    repositories = []
    print("Fetching repositories...")  # Start message
    for user in users:
        login = user['login']
        page = 1
        while True:
            # Fetch repositories for each user
            url = f"https://api.github.com/users/{login}/repos?per_page=500&page={page}"
            response = requests.get(url, headers=headers)
            repos_data = response.json()
            
            if not repos_data:  # No more repositories
                break
            
            for repo in repos_data:
                repositories.append({
                    'login': login,
                    'full_name': repo['full_name'],
                    'created_at': repo['created_at'],
                    'stargazers_count': repo['stargazers_count'],
                    'watchers_count': repo['watchers_count'],
                    'language': repo['language'],
                    'has_projects': repo['has_projects'],
                    'has_wiki': repo['has_wiki'],
                    'license_name': repo['license']['name'] if repo.get('license') is not None else ''
                })
            
            print(f"Fetched {len(repos_data)} repositories for {login} (page {page})...")  # Progress update
            page += 1  # Fetch next page
    
    # Save to repositories.csv
    repos_df = pd.DataFrame(repositories)
    repos_df.to_csv('repositories.csv', index=False)
    print("Repository data saved to repositories.csv")  # Completion message

if __name__ == "__main__":
    fetch_users()
    # Load the users from the CSV to fetch repositories
    users_df = pd.read_csv('users.csv')
    fetch_repositories(users_df.to_dict(orient='records'))





# from config import GITHUB_TOKEN
# import requests
# import pandas as pd

# headers = {'Authorization': f'token {GITHUB_TOKEN}'}

# # Your existing functions: fetch_users, fetch_repositories, etc.


# def fetch_users():
#     users = []
#     page = 1
#     while True:
#         # Search for users in Toronto with more than 100 followers
#         url = f"https://api.github.com/search/users?q=location:Toronto+followers:>100&page={page}"
#         response = requests.get(url, headers=headers)
#         data = response.json()
        
#         # Break if there are no more users
#         if 'items' not in data or not data['items']:
#             break
        
#         for user in data['items']:
#             users.append({
#                 'login': user['login'],
#                 'name': user.get('name', ''),
#                 'company': user.get('company', '').strip('@ ').upper(),
#                 'location': user.get('location', 'Toronto'),
#                 'email': user.get('email', ''),
#                 'hireable': user.get('hireable', ''),
#                 'bio': user.get('bio', ''),
#                 'public_repos': user.get('public_repos', 0),
#                 'followers': user.get('followers', 0),
#                 'following': user.get('following', 0),
#                 'created_at': user.get('created_at', '')
#             })
        
#         page += 1  # Fetch next page

#     # Save to users.csv
#     users_df = pd.DataFrame(users)
#     users_df.to_csv('users.csv', index=False)

# def fetch_repositories(users):
#     repositories = []
#     for user in users:
#         login = user['login']
#         page = 1
#         while True:
#             # Fetch repositories for each user
#             url = f"https://api.github.com/users/{login}/repos?per_page=500&page={page}"
#             response = requests.get(url, headers=headers)
#             repos_data = response.json()
            
#             if not repos_data:  # No more repositories
#                 break
            
#             for repo in repos_data:
#                 repositories.append({
#                     'login': login,
#                     'full_name': repo['full_name'],
#                     'created_at': repo['created_at'],
#                     'stargazers_count': repo['stargazers_count'],
#                     'watchers_count': repo['watchers_count'],
#                     'language': repo['language'],
#                     'has_projects': repo['has_projects'],
#                     'has_wiki': repo['has_wiki'],
#                     'license_name': repo['license']['name'] if repo.get('license') is not None else ''
#                 })
            
#             page += 1  # Fetch next page
    
#     # Save to repositories.csv
#     repos_df = pd.DataFrame(repositories)
#     repos_df.to_csv('repositories.csv', index=False)


# if __name__ == "__main__":
#     fetch_users()
#     # Load the users from the CSV to fetch repositories
#     users_df = pd.read_csv('users.csv')
#     fetch_repositories(users_df.to_dict(orient='records'))




# from config import GITHUB_TOKEN
# import requests
# import pandas as pd

# headers = {'Authorization': f'token {GITHUB_TOKEN}'}

# def fetch_users():
#     users = []
#     page = 1
#     print("Fetching users...")  # Start message
#     while True:
#         # Search for users in Toronto with more than 100 followers
#         url = f"https://api.github.com/search/users?q=location:Toronto+followers:>100&page={page}"
#         response = requests.get(url, headers=headers)
#         data = response.json()
        
#         # Break if there are no more users
#         if 'items' not in data or not data['items']:
#             break
        
#         for user in data['items']:
#             users.append({
#                 'login': user['login'],
#                 'name': user.get('name', ''),
#                 'company': user.get('company', '').strip('@ ').upper(),
#                 'location': user.get('location', 'Toronto'),
#                 'email': user.get('email', ''),
#                 'hireable': user.get('hireable', ''),
#                 'bio': user.get('bio', ''),
#                 'public_repos': user.get('public_repos', 0),
#                 'followers': user.get('followers', 0),
#                 'following': user.get('following', 0),
#                 'created_at': user.get('created_at', '')
#             })
        
#         print(f"Fetched page {page}...")  # Progress update
#         page += 1  # Fetch next page

#     # Save to users.csv
#     users_df = pd.DataFrame(users)
#     users_df.to_csv('users.csv', index=False)
#     print("User data saved to users.csv")  # Completion message

# def fetch_repositories(users):
#     repositories = []
#     print("Fetching repositories...")  # Start message
#     for user in users:
#         login = user['login']
#         page = 1
#         while True:
#             # Fetch repositories for each user
#             url = f"https://api.github.com/users/{login}/repos?per_page=500&page={page}"
#             response = requests.get(url, headers=headers)
#             repos_data = response.json()
            
#             if not repos_data:  # No more repositories
#                 break
            
#             for repo in repos_data:
#                 repositories.append({
#                     'login': login,
#                     'full_name': repo['full_name'],
#                     'created_at': repo['created_at'],
#                     'stargazers_count': repo['stargazers_count'],
#                     'watchers_count': repo['watchers_count'],
#                     'language': repo['language'],
#                     'has_projects': repo['has_projects'],
#                     'has_wiki': repo['has_wiki'],
#                     'license_name': repo['license']['name'] if repo.get('license') is not None else ''
#                 })
            
#             print(f"Fetched {len(repos_data)} repositories for {login} (page {page})...")  # Progress update
#             page += 1  # Fetch next page
    
#     # Save to repositories.csv
#     repos_df = pd.DataFrame(repositories)
#     repos_df.to_csv('repositories.csv', index=False)
#     print("Repository data saved to repositories.csv")  # Completion message

# if __name__ == "__main__":
#     fetch_users()
#     # Load the users from the CSV to fetch repositories
#     users_df = pd.read_csv('users.csv')
#     fetch_repositories(users_df.to_dict(orient='records'))


