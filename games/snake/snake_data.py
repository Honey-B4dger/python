from matplotlib import pyplot as plt
import csv

with open('data/log.csv') as f:
    data = []
    for row in csv.reader(f):
        data.append(row)

lengths = []

for row in data:
    lengths.append(int(row[4]))

print(lengths)

fig, ax = plt.subplots()

ax.hist(lengths)

plt.show()



