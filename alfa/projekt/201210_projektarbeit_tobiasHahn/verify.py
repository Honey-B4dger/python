files = [
    'easiest',
    'intermediate',
    'wikipedia',
]

results = {}

for file in files:
    with open('solutions/' + file + '.csv') as f:
        solution = f.read()

    with open('data/' + file + '_solution.csv') as f:
        calculation = f.read()

    results[file] = solution == calculation

print('+=================+===========+')
print('| grid            |  result   |')
print('+-----------------+-----------+')
for key, value in results.items():
    if value == 1:
        output = 'verified'
    else:
        output = 'not verified!'
    print(f'| {key:15} |  {output:8} |')
print('+-----------------+-----------+')

