import os
from datetime import datetime

class Age():
    def __init__(self):
        self.entries = int()
        self.ages = {}

    # Bildschirm bereinigen
    @staticmethod
    def clear():
        os.system('clear')

    # Fortsetzen beim Drücekn der Eingabetaste
    @staticmethod
    def continue_():
        input('\nZum Fortsetzen Enter drücken... ')

    # Begruessung
    def greet(self):
        Age.clear()
        print(f'\nHiermit wird eine Liste von Personen und deren Alter erzeugt.')

        # Hinweis zum Abbrechen angeben
        print(f'\nZum Abbrechen "q" eingeben.')
        Age.continue_()
        Age.clear()

    # Name und Alter entgegennemen
    def get_input(self):
        while True:
            new_entry = {}
            name = input(f'\nWie heißt du? ').title()
            # Pruefung, ob die Eingabe mit q beendet werden soll
            if name == 'Q':
                break
            # Pruefung, ob der Name nur aus Buchstaben besteht
            while not name.isalpha():
                name = input(f'\nBitte gib nur Buchstaben ein. ').title()

            # Pruefung, ob der Name bereits als Schluessel vergeben ist
            if name in self.ages.keys():
                print(f'Der Name "{name}" ist bereits vergeben. :(')
                continue

            alter = input (f'\nWie alt bist du, {name}? ')
            # Pruefung, ob das Alter eine Zahl von 0 bis 100ist
            while not alter in [str(i) for i in range(0,101)]:
                alter = input (f'\nBitte gib ein zulässiges Alter an, {name}! ')

            # dem User die Moeglichkeit geben, die Eingaben zu pruefen
            message = f'\nDu heißt {name} und bist {alter} Jahre alt? y/n '
            confirm = input(message)
            while confirm not in ('y', 'n',):
                confirm = input('Bitte gib y oder n an: ')
            if confirm == 'y':
                pass
            else:
                print('\nDie Eingaben werden NICHT übernommen...')
                print(80 * '-')

                continue

            # Zeitstempel
            zeitpunkt = datetime.now()
            # Werte zusammenfuehren
            new_entry['alter'] = alter
            new_entry['zeit'] = str(zeitpunkt)[:19]
            # die Eingabe bestaetigen und ins dictionary uebernehmen
            print('\nDie Eingaben werden übernommen...')
            self.ages[name] = new_entry
            self.entries = len(self.ages.keys())
            print(80 * '-')

    # die Eintraege in schoener Form widergeben
    def print_entries(self):
        Age.clear()
        p_c = lambda lst: print('| '+' | '.join([el.ljust(20) for el in lst])+' |')

        print(f'\nFolgende Personen haben sich eingetragen:')

        header = ['NAME', 'ALTER', 'ZEIT']
        print('\n' + 70 * '=')
        p_c(header)
        print('+' + 68 * '-' + '+')
        for k, v in self.ages.items():
            output = [k, str(v['alter']), v['zeit']]
            p_c(output)
        print(70 * '=')
