import csv

with open('geburtstage.csv') as f:
    content = csv.reader(f)
    print(f'Titel-Zeile: {" ".join(next(content))}')

    for y, row in enumerate(content, 1):
#        if y == 0:
#            continue
        print(f'{y}. Name: {row[0]}')
