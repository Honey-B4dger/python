import json

data = [{'foo' : 1},
        {'bar': 'spam'},
        {'eggs': False},
       ]
with open('json_test.json', 'w') as f:
    f.write(json.dumps(data, indent=4))
    #json.dumps(f, data)
