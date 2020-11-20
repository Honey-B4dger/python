import os

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

wochen = list(range(1,6))

# Iterieren über die Wochen
for woche in wochen:
    # termin ist der index des Wochentags, an dem der Termin stattfindet
    if woche % 2 == 1:
        termin = 2
    else:
        termin = 4

    # Iterieren über die einzelnen Tage
    for i_tag, tag in enumerate(wochentage):
        # kurze Info zu aktueller Woche und aktuellem Tag
        print(f'\nEs ist Woche {woche} ', end = '')
        print(f'und heute ist {tag}.')

        # Delta in Tagen bis zum Termin bestimmen
        delta = i_tag - termin
        # Negatives Vorzeichen und kleiner -1: Termin ist in der Zukunft
        if delta < -1:
            print(f'Es sind noch {-delta} Tage bis zum Termin ', end = '')
            print(f'am {wochentage[termin]}')
        # Delta == -1: nur noch ein Tag
        elif delta == -1:
            print(f'Der Termin ist am morgigen {wochentage[termin]}.')
        # Delta == 0: Termin ist heute 
        elif delta == 0:
            print(f'Der Termin ist heute!')
        # ansonsten: Termin ist bereits verstrichen
        else:
            print('Der Termin ist schon verstrichen.')

    print('\n' + 80 * '=')

