import pickle
import urllib.request

url = 'http://www.pythonchallenge.com/pc/def/banner.p'

data = pickle.load(urllib.request.urlopen(url))

for line in range(len(data)):
    output = ''
    for tupel in range(len(data[line])):
        #print(data[line][tupel])
        symbol, repetition = data[line][tupel]
        output += symbol * repetition
    print(output)
