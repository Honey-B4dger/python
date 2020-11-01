import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

#ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

data = pd.read_csv('data_hist.csv')
median_age = 29

print(data.size)
print(data.head())


ids = data['Responder_id']
ages = data['Age']

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, edgecolor='black', log=True)
plt.axvline(median_age, label='Age Median', color='red')

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()
plt.show()
