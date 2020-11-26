from matplotlib import pyplot as plt
import numpy as np

with open ('daten_mod.csv') as f:
    data = []
    for row in f:
        temp = []
        values = row.split(',')
        for value in values:
            temp.append(float(value))
        data.append(temp)

labels = ['linear', 'increment 2', 'increment 3', 'sum']
axes = [0, 100, 0, 600]
plt.xticks(np.arange(0,101,10))
plt.yticks(np.arange(0,601,50))
plt.minorticks_on()

x = [row[0] for row in data]

for i in range(4):
    plt.plot(x, [row[i] for row in data], label = labels[i])

plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.axis(axes)

plt.grid(color = 'black', alpha = 0.2, linestyle = '-')

plt.show()

