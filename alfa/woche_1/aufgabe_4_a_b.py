import os

os.system('clear')

########################################################################

print('')
print('Aufgabenteil a:')
print('')

tage = ['Montag',
        'Dienstag',
        'Mittwoch',
        'Donnerstag',
        'Freitag',
        'Samstag',
        'Sonntag',]

farben = ['Grün',
        'Rot',
        'Gelb',
        'Blau',
        'Lila',
        'Magenta',
        'Rosa',]

for index, tag in enumerate(tage):
        print(f'Meine Lieblingsfarbe für {tag}e ist {farben[index]}.')

print('\n' + '=' * 72 + '\n')

########################################################################

print('Aufgabenteil b:')
print('')

print('Erste Liste:')

liste_1 = [i for i in range(1,11)]
print(liste_1)

print('')

print('Zweite Liste:')

liste_2 = [i for i in range(1,12, 2)]
print(liste_2)
print('')

liste_2_alt = [i for i in range(1,12) if i % 2 != 0]
print('alternativ:')
print(liste_2_alt)

print('\n' + '=' * 72 + '\n')
