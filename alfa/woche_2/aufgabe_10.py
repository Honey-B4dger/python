import os
import time

#die Daten daten.csv zum Schreiben oeffnen
#t_start = time.time()
with open('daten.csv', 'w') as f:
    #fuer die Zahlen 1 bis 100 die geforderten Zahlenreihen erzeugen
    for i in range(0, 100):
        temp = []
        base = float(i)
        # durch einen Faktor die Inkremente anpassen
        for factor in range(1,4):
            temp.append(base * factor + 1)
        #und die entsprechende Zeile mit \n schreiben
        f.write(','.join([str(num) for num in temp]) + '\n')

#os.system('cat daten.csv')

with open('daten.csv', 'r') as f:
    content = []
    for line in f:
        content.append(line.strip().split(','))

with open('daten_mod.csv', 'w') as f:
    for line in content:
        summe = sum([float(element) for element in line])
        line.append(summe)
        strngs = [str(element) for element in line]
        f.write(','.join(strngs) + '\n')

os.system('cat daten_mod.csv')

#for line in content:
#    print(line)
#
#with open('timings.txt', 'a') as f:
#    f.write(f'{max_number} took {round(time.time() - t_start)} s' + '\n')
#
#os.system('cat timings.txt')

