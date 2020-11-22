import connect4
import os

version = 'Vier Gewinnt V. 0.8'

clear = lambda: os.system('clear')
conti = lambda: input('Zum Fortsetzen bitte die Eingabetaste drücken...')

c = connect4.Connect4()

clear()

print(version)
print('')

print('Hallo, ich möchte eine Runde Vier Gewinnt spielen')
print('')
conti()
clear()


alternator = 0
while c.game_over == False:
    c.print_playfield()
    print('')
    choice = input('In welche Spalte möchtest du werfen? ')
    if len(choice) == 1 and choice.isnumeric():
        choice = int(choice)
        if c.topped[choice - 1] == False and choice in range(1,8,1):
            if alternator % 2 == 0:
                c.drop(choice - 1, 'X')
            else:
                c.drop(choice - 1, 'O')
    else:
        print('Versuche eine andere Spalte!')

    c.create_slices()
    c.check_slices()
    c.check_tops()



    alternator += 1
    conti()
    clear()

if c.game_over and c.four_in_a_row:
    print('Gratulation. Vier in einer Reihe!')
    print('')
elif c.game_over and c.topped_off:
    print('Unentschieden. -.-')
    print('')
