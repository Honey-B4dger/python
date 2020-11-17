import os

os.system('clear')

liste = []

print('Aufgabenteil c:')
print('')

vorname = input('Bitte gib deinen Vornamen an: ')
nachname = input ('Und jetzt noch dein Nachname: ')

liste.append(vorname.title())
liste.append(nachname.title())

print('')
print(f'Hallo, {liste[0]} {liste[1]}!')

print('')

print('alternativ mit join():')
print('Hallo, ' + ' '.join(liste) + '!')


