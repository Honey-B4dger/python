"""
dict = {'Fahrradmanufaktur': 1000,
        'Harisson': 500,
        'Spam': 200,
        'Eggs': 2000,
       }

#print(dict)

for key, value in dict.items():
    print(f'Hersteller: {key}, Preis: {value} €')

print('')

for key, value in sorted(dict.items()):
    print(f'Hersteller: {key}, Preis: {value} €')

print('')

for key, value in sorted(dict.items(), key = lambda item: item[1]):
    print(f'Hersteller: {key}, Preis: {value} €')

"""

bicycles = {
    'Kalkhoff': ['Master', 'Experteer',],
    'Kreidler': ['4Runner',],
    'Bullet': ['Gopro', 'Hike',],
    'VanMoof': ['StreetRunner', 'CityGo',]
    }

for make, names in bicycles.items():
    print(f'{make}: ')
    for name in names:
        print(f'\t- {name}')

keys = []

for key in bicycles.keys():
    keys.append(key)

print(keys)
