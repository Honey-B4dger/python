import csv

with open('data_short.csv') as f:
    content = csv.reader(f, delimiter = ',')
    data = {}
    labels = next(content)
    for label in labels:
        data[label] = []
    for row in content:
        print(row)
        for x, column in enumerate(row):
            data[labels[x]].append(int(column))

print(data)

