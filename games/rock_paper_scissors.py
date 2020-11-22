import os
os.system('clear')
print('Hallo Maus, lass uns eine Runde Schere, Stein, Papier spielen!')
input('\nWeiter mit der Eingabetaste... ')
while True:
    os.system('clear')
    eingabe = input('Schere, Stein oder Papier? ').lower()
    if eingabe not in ('schere', 'stein', 'papier',):
        print('Bitte gib etwas zulässiges ein!')
        input('\nWeiter mit der Eingabetaste... ')
        continue
    if eingabe == 'schere':
        print('Stein. Du hast VERLOREN! :P')
    elif eingabe == 'stein':
        print('Papier. Du hast VERLOREN! :P')
    else:
        print('Schere. Du hast VERLOREN! :P')

    input('\nDrücke Enter für eine neue Runde... ')
