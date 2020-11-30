import json

with open('kap_13_Pegel_Bonn.json') as f:
    data = json.load(f)

print(data[0].keys())

for row in data:
    for key, value in row.items():
        print(key, value)
