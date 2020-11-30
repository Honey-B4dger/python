import json
from matplotlib import pyplot as plt
import cartopy.crs as ccrs

#json-datei oeffnen
with open('eq_data_30_day_m1.json') as f:
    data = json.load(f)

print(type(data))
print(data.keys())

with open('readable_eq_data', 'w') as f:
    json.dump(data, f, indent=4)

lats, longs, mags = [], [], []

for row in data['features']:
    mags.append(row['properties']['mag'])
    lats.append(row['geometry']['coordinates'][0])
    longs.append(row['geometry']['coordinates'][1])

#Groessenordnungen skalieren
mags_scl = [(10**mag)/1000 for mag in mags]

ax = plt.axes(projection = ccrs.PlateCarree())
#ax.stock_img()
ax.coastlines(linewidth=0.3)
ax.coastlines(linewidth=0.3)

ax.set_xlabel('Latitude [°]')
ax.set_ylabel('Longitude [°]')

ax.scatter(lats, longs, c=mags, cmap=plt.cm.rainbow, s = [mags_scl], alpha=.7,
          edgecolors='none')

#for y, lat in enumerate(lats):
#    plt.annotate(str(round(mags[y], 1)), (lat, longs[y]))

plt.savefig('earthquakes.pdf', dpi=500)
plt.show()
