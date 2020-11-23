import os
import c4_functions as c4f

# einfache Funktion für 'clear'
cls = lambda: os.system('clear')

continue_ = lambda: input('\nZum Fortsetzen die Eingabetaste drücken... ')

# Spielfeld initialisieren
def grid_init():
    for row in range(6):
        row_temp =[]
        for column in range(7):
            row_temp.append(' ')
        grid.append(row_temp)

def get_players():
    players = []
    for i in range(1, 3):
        while True:
            cls()
            name = input(f'Spieler {i}, wie heißt du? ').title()
            if name.isalpha():
                confirmation = input(f'Du heißt {name}? [j/n] ')
                if confirmation == 'j':
                    players.append(name)
                    break
                else:
                    continue
            else:
                continue
    return players

def print_title():
    print(f'<<< 4 Gewinnt - {players[0]} gegen {players[1]} >>>')
    print('')

# das aktuelle Spielfeld ausgeben
def grid_print():
    print('')
    print('  ' + '   '.join([str(i) for i in range(1,8)]))
    separator = lambda: print('+' + 7 * '---+')
    separator()
    for y, line in enumerate(grid, 1):
        print('| ' + ' | '.join(line) + ' |')
        separator()

def drop(column, turn, symbol):
    column -= 1
    if turn % 2 == 0:
        symbol = 'O'
    else:
        symbol = 'X'
    v_slice = [row[column] for row in grid]

    for y in range(-1, -7, -1):
        value = v_slice[y]
        if value == ' ':
            grid[y][column] = symbol
            return True
        if y == -6 and value != ' ':
            return False

def status_print():
    print(f'\nRunde: {turn}')
    print(f'4 in einer Reihe: {connected_4}')
    print(f'Spielfeld voll: {topped_off}')

if __name__ == '__main__':

    grid = []
    turn = 0
    symbols = ['O', 'X']
    connected_4 = False
    game_over = False
    topped_off = False

    grid_init()
    cls()
    print('Hallo, lasst uns eine Runde 4 GEWINNT spielen!')
    continue_()
    players = get_players()

    while True:
        player = players[turn%2]
        symbol = symbols[turn%2]

        cls()
        print_title()
        print(f'{player}, du bist an der Reihe. ', end ='')
        print(f'Du spielst mit {symbol}.')
        grid_print()
        topped_off = c4f.topped_off(grid)

        while True:
            spalte = input(f'\nIn welche Spalte möchtest du werfen? ')
            if spalte in [str(i) for i in range(1,8)]:
                drop(int(spalte), turn, symbol)
                break
            else:
                continue

        #continue_()
        connected_4 = c4f.check_grid(grid)
        topped_off = c4f.topped_off(grid)

        #status_print()
        if connected_4 or topped_off:
            break
        else:
            turn += 1

    print('Game Over.')
    cls()
    print_title()
    grid_print()

    if not connected_4 and topped_off:
        print('Unentschieden.')
    else:
        print('\n4 in einer Reihe!')
        print(f'\n{player} gewinnt.')
