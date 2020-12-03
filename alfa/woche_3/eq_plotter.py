import json
from matplotlib import pyplot as plt
import cartopy.crs as ccrs
import os

class eqPlotter():
    def __init__(self, filename):
        self.filename = filename
        self.data = {}

    def open_file(self):
        with open(os.path.expanduser(self.filename)) as f:
            self.data = json.load(f)

    def print_readable(self):
        with open('readable_eq_data.json', 'w') as f:
            features = self.data['features']
            json.dump(features[0], f, indent=4)
            os.system('cat readable_eq_data.json')

    def plot_data(self):
        lats, longs, mags = [], [], []

        for row in self.data['features']:
            mags.append(row['properties']['mag'])
            lats.append(row['geometry']['coordinates'][0])
            longs.append(row['geometry']['coordinates'][1])

        #Groessenordnungen skalieren
        mags_scl = [(10**mag)/1000 for mag in mags]

        ax = plt.axes(projection = ccrs.PlateCarree())
        ax.stock_img()
        ax.coastlines(linewidth=0.3)
        ax.coastlines(linewidth=0.3)

        ax.set_xlabel('Latitude [deg]')
        ax.set_ylabel('Longitude [deg]')

        ax.scatter(lats, longs, c=mags, cmap=plt.cm.rainbow, s = [mags_scl], alpha=.7,
                  edgecolors='none')

        #for y, lat in enumerate(lats):
        #    plt.annotate(str(round(mags[y], 1)), (lat, longs[y]))

        plt.savefig('earthquakes.pdf', dpi=500)
        plt.show()
