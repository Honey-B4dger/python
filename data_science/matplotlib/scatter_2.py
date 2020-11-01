from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

#plt.style.use('seaborn')
plt.xkcd()

data = pd.read_csv('2019-05-31-data.csv')

view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

print(data.head(5))
print(data.size)
print(data.shape)

plt.scatter(view_count, likes, c=ratio, cmap='summer', edgecolor='black', linewidth=1,
           alpha=0.75)

cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')
#cbar = plt.colorbar()
#cbar.set_label('Satisfaction')

plt.xscale('log')
plt.yscale('log')

plt.title('Trending Youtube-Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()
plt.show()
