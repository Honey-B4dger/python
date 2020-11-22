import os
from slicer import *

# einfache Funktion für 'clear'
cls = lambda: os.system('clear')

continue_ = lambda: input('Zum Fortsetzen die Eingabetaste drücken. ')

# Spielfeld initialisieren
def grid_init():
    for row in range(6):
        row_temp =[]
        for column in range(7):
            row_temp.append(' ')
        grid.append(row_temp)

# das aktuelle Spielfeld ausgeben
def grid_print():
    separator = lambda: print('+' + 7 * '---+')
    separator()
    for y, line in enumerate(grid, 1):
        print('| ' + ' | '.join(line) + ' |')
        separator()

def drop(column):
    global turn
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

def topped_off(grid):
    if ' ' in grid[0]:
        return False
    else:
        return True



if __name__ == '__main__':

    grid = []
    turn = 0
    players = ['Spieler 1', 'Spieler 2',]
    connected_4 = False
    game_over = False
    topped_off = False
    grid_init()
    cls()

    while not connected_4 and not game_over:
        player = players[turn%2]

        cls()
        print(f'{player} ist an der Reihe.')
        print(f'Runde: {turn}')
        grid_print()

        spalte = int(input(f'In welche Spalte möchtest du werfen'))
        drop(spalte)

        print(check_grid(grid))

        continue_()

        turn += 1
