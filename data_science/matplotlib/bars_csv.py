from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter
import pandas as pd

plt.style.use('fivethirtyeight')
#plt.xkcd()

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data ['LanguagesWorkedWith']

#with open('data.csv', 'r') as csv_file:
#    csv_reader = csv.DictReader(csv_file)
#
#    language_counter = Counter()
#
#    for row in csv_reader:
#        language_counter.update(row['LanguagesWorkedWith'].split(';'))


language_counter = Counter()

for response in lang_responses:
    language_counter.update(response['LanguagesWorkedWith'].split(';'))

languages = []
popularity = []
#print(language_counter.most_common(15))

for item in language_counter.most_common(15):
    lan,pop = item
    languages.append(lan)
    popularity.append(pop)

languages.reverse()
popularity.reverse()
#languages = languages[::-1]
#popularity = popularity[::-1]

plt.barh(languages, popularity)



plt.title('Most Popular Languages')
plt.xlabel('Number of Users')
#plt.ylabel('Programming Language')
#
#plt.xticks(ticks=x_indexes, labels=ages_x)
#
#plt.legend()
plt.tight_layout()
#
##plt.savefig('plot.emf')
#
##plt.grid(True)
plt.show()


