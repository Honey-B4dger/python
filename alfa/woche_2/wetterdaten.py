import csv
from matplotlib import pyplot as plt
from datetime import date, time, datetime

with open('mpi_saale.csv') as f:
    csv_reader = csv.reader(f, delimiter = ',')

    labels = [el.strip() for el in next(csv_reader)]
    channels = [el.split()[0] for el in labels]

    data = {}

    for channel in channels:
        data[channel] = []

    print(data)
    #print([el.strip() for el in next(csv_reader)])
    #print(next(csv_reader).split().strip())
    for row in csv_reader:
        for i, element in enumerate(row):
            if i == 0:
                raw = element.strip()
                date = datetime.strptime(raw, '%d.%m.%Y %H:%M:%S') 
                data[channels[i]].append(date)
            else:
                data[channels[i]].append(float(element.strip()))

print(data.keys())

plt.xkcd()
plt.figure(figsize=(7,5))

res = plt.subplot(2,1,1)
plt.plot(data['Date'], data['T'], color = 'r', label = 'Temperatur')
plt.ylabel('Temperatur')
plt.xlabel('Datum')
plt.xticks([15,20])
plt.grid()

plt.subplot(2,1,2)
plt.plot(data['Date'], data['rh'], color = 'b', label = 'relative Feuchte')
plt.ylabel('relative Feuchte')
plt.grid

#plt.legend()

plt.gcf().autofmt_xdate()

plt.show()
