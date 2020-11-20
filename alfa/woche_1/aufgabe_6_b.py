import os
import sys

os.system('clear')

wochentage = [
    'Montag',
    'Dienstag',
    'Mittwoch',
    'Donnerstag',
    'Freitag',
    'Samstag',
    'Sonntag',
]

startzeiten = []

# für jeden Tag der Woche die Uhrzeit des ersten Kaffes erfragen
for wochentag in wochentage:
    startzeit = input(f'\nWann trinkst du {wochentag.lower()}s den Ersten Kaffe?\n')
    # falls die Eingabe keine ganze Zahl ist, erneut nachfragen
    if startzeit.isdigit() == False:
        startzeit = input(f'\nBitte gib eine ganze Zahl an.\n')
        # falls wieder unzulaessig -> Programm beenden
        if startzeit.isdigit() == False:
            print('Bitte gib das nächste Mal nur eine ganze Zahl an.')
            print('Das Programm wird jetzt beendet.')
            sys.exit()


    startzeiten.append(startzeit)

# Trennlinie ausgeben
print('\n' + 80 * '=')

print('\n Den ersten Kaffe des Tages trinkst du:\n')

# ordentlich lesbar die ersten Kaffees ausgeben
for index, wochentag in enumerate(wochentage):
    print(f'\t- {wochentag.lower()}s um {startzeiten[index]} Uhr.')

# die spaeteste Zeit fuer einen Kaffee bestimmen
latest = max(startzeiten)

# Pruefung, an welchen Tagen die spaeteste Zeit vorkommt
res = []
for index, startzeit in enumerate(startzeiten):
    if startzeit == latest:
        res.append(wochentage[index])


# Liste der Tage, klein und mit "s" -> montags, dienstag...
appendix = ''
for index, tag in enumerate(res):
    tag = f'{tag.lower()}s'
    res[index] = tag

# Resultate mit join() zusammenfuegen
print(f'\n Den letzten Kaffe trinkst du ', end = '')
print(' und '.join(res), end = '')
print(f' um {latest} Uhr.')

print('')
