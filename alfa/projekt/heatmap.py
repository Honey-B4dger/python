from matplotlib import pyplot as plt
from matplotlib import cm
import json

class Heatmap():
    def __init__(self, file):
        self.file = file
        self.data = {}

    def plot_data(self):

        with open('data/' + self.file + '_data.json') as f:
            self.data = json.load(f)

        fig = plt.figure()
        ax = plt.axes()

        frequencies = self.data['frequencies']
        iterations = self.data['iterations']
        time = self.data['time']

        im = ax.imshow(frequencies, cmap=cm.rainbow)
        ax.set_xlabel('Spalte')
        ax.xaxis.set_label_position('top')
        ax.set_ylabel('Zeile')

        ax.set_title(f'{self.file}.csv, solved after {iterations} iterations in {time} s')

        ax.set_xticks([i for i in range(9)])

        fig.colorbar(im, ax=ax)

        plt.savefig('data/' + self.file + '.png')
