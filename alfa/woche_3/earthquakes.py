import json

with open('eq_data_1_day_m1.json') as f:
    eq_data = json.load(f)

print(type(eq_data))

main_keys = eq_data.keys()
print(main_keys)

print(type(eq_data['features']))
print(type(eq_data['features'][0]))
print(eq_data['features'][0].keys())
print(eq_data['features'][0]['properties'].keys())
