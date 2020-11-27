from matplotlib import pyplot as plt

x_values = [x for x in range(100001)]
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s = 10)

plt.show()


