from matplotlib import pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('classic')
    fig, axs = plt.subplots(2)
    print(list(axs))
    print(axs[0])
    point_numbers = range(rw.num_points)
    axs[0].scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=15)
    axs[0].scatter(0,0, c='green', edgecolors='none', s=100)
    axs[0].scatter(rw.x_values[-1], rw.y_values[-1], c='r', edgecolors='none',
               s=100)

    axs[0].get_xaxis().set_visible(False)
    axs[0].get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk? [y/n] ')
    if keep_running == 'n':
        break
