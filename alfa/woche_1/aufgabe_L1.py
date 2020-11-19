colors = [
    'red',
    'blue',
    'green',
    'yellow',
    'blue',
    'cyan',
    'magenta',
    'blue',
    'orange',
    'black',
    ]

print(f'\nDie Liste der Farben hat {len(colors)} Elemente')

blues = colors.count('blue')

print(f'\nDie Farbe "blue" kommt {blues} Mal vor.')

blues_indices = []
for index, color in enumerate(colors):
    if color == 'blue':
        blues_indices.append(index)

print('\n"blue" kommt an folgenden Indices vor: ', end = '')
print(', '.join([str(i) for i in blues_indices]))


print(f'\nDie Farben sind: ' + ', '.join(colors))

print(f'\nDie vorkommenden Farben sind: ' + ', '.join(sorted(set(colors))))
print('')

for index, color in enumerate(colors):
    print(f'{index}: {color}')


