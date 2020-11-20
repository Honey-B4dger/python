import os
from datetime import datetime

os.system('clear')

ages = {}

# Begruessung
print(f'\nHiermit wird eine Liste von Personen und deren Alter erstellt.')

# Hinweis zum Abbrechen angeben
print(f'\nZum Abbrechen "q" eingeben.')
input('Zum Fortsetzen Enter drücken...')
os.system('clear')

# Name und Alter entgegennemen
while True:
    new_entry = {}
    name = input(f'\nWie heißt du? ').title()
    # Pruefung ob die Eingabe mit q beendet werden soll
    if name == 'Q':
        break
    # Pruefung, ob der Name nur aus Buchstaben besteht
    while not name.isalpha():
        name = input(f'\nBitte gib nur Buchstaben ein. ').title()

    # Pruefung, ob der Name bereits als Schluessel vergeben ist
    if name in ages.keys():
        print(f'Der Name "{name}" ist bereits vergeben. :(')
        continue

    alter = input (f'\nWie alt bist du, {name}? ')
    # Pruefung, ob das Alter eine Zahl von 0 bis 100ist
    while not alter in [str(i) for i in range(0,101)]:
        alter = input (f'\nBitte gib ein zulässiges Alter an, {name}! ')

    # dem User die Moeglichkeit geben, die Eingaben zu pruefen
    message = f'\nDu heißt {name} und bist {alter} Jahre alt. Korrekt? y/n '
    confirm = input(message)
    while confirm not in ('y', 'n',):
        confirm = input('Bitte gib y oder n an: ')
    if confirm == 'y':
        pass
    else:
        continue

    # Zeitstempel
    zeitpunkt = datetime.now()
    # Werte zusammenfuehren
    new_entry['alter'] = alter
    new_entry['zeit'] = 'foo'
    # die Eingabe bestaetigen und ins dictionary uebernehmen
    print('\nDie Eingaben werden übernommen...')
    ages[name] = new_entry
    print(80 * '-')

# die Eintraege in schoener Form widergeben
os.system('clear')
print(f'\nFolgende Personen haben sich eingetragen:')

print('\n' + 49 * '=')
print('| NAME' + '\t\t| ' + 'ALTER' + '\t\t|' + 'ZEIT' + '\t\t|')
print('+' + 47 * '-' + '+')
for key, value in ages.items():
    print('| ' + '\t\t| '.join([key, str(value['alter']), '3',]) + '\t\t|')
print(49 * '=')


