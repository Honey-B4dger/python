from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from matplotlib import cm
import csv

file = 'wikipedia.log'
data = {}

with open(file) as f:
    content = csv.reader(f)
    labels = next(content)

    for label in labels:
        data[label] = []

    for row in content:
        for column, value in enumerate(row):
            label = labels[column]
            data[labels[column]].append(int(value))

fig = plt.figure()
ax = plt.axes(projection='3d')

rows = data['row']
columns = data['column']
iterations = data['iteration']

ax.plot3D(rows, columns, iterations, c=iterations, cmap=cm.rainbow, alpha=.5)
ax.set_xlabel('row')
ax.set_ylabel('column')
ax.set_zlabel('iteration')

#axs.scatter(data['iteration'], data['value'])

plt.show()

