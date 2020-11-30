import json
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

response_dict = r.json()

#print(response_dict.keys())

print(f"Total number of repos: {response_dict['total_count']}")

repo_dicts = response_dict['items']

print(f"Repos returned: {len(repo_dicts)}")

repo_dict = repo_dicts[0]

print(type(repo_dict))
with open('readable_dict', 'w') as f:
    json.dump(repo_dict, f, indent=4)

print(f"\nkeys: {repo_dict.keys()}")
