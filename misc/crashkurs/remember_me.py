import json

filename = 'username.json'





username = input('What is your username? ')

with open(filename, 'w') as f:
    json.dump(username, f)
    print(f' We will remember you, {username}!')
