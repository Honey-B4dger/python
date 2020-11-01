from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
#plt.xkcd()


# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0,0,0.1,0]

#slices = [120, 80, 30, 20]
#labels = ['60','40', 'Extra1', 'Extra2']
##colors = ['blue', 'red', 'yellow', 'green']

plt.pie(slices, labels=labels, wedgeprops={'edgecolor':'black'},
        explode=explode, shadow=True, startangle=90, autopct='%1.1f%%')

plt.title('Pie Chart')
plt.tight_layout()
plt.show()
