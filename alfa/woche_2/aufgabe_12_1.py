import csv
from matplotlib import pyplot as plt

with open('daten_mod.csv') as f:
    csv_reader = csv.reader(f)

    labels = [el.strip() for el in next(csv_reader)]

    data = []
    for line in csv_reader:
        temp = []
        for value in line:
            temp.append(float(value.strip()))
        data.append(temp)

data_formatted = [[] for i in range(len(labels))]

for row in data:
    for i, value in enumerate(row):
        data_formatted[i].append(value)

for i in range(1,4):
    plt.plot(data_formatted[0], data_formatted[i], label = labels[i])

plt.legend()


plt.show()
