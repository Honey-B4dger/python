import csv
import os
import sys
import json
import time
from heatmap import Heatmap
from sudoku import Sudoku


def greet():
    print('This is is a solver for Sudokus. ')

def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def get_filenames():
    pass

def continue_():
    input('\nPress return to continue... ')

def print_help():
    print('\nYou can use the following commands:')
    print('')
    commands = [
        'add <filename> \t-> add a file to files',
        'remove <filename> \t-> remove a file from files',
        'files \t\t-> print the files added to files',
        'print <filename> \t-> print a file in the terminal',
        'list \t\t\t-> print a file from grids/',
        'quit \t\t\t-> quit the program',
        'solve \t\t-> start the solving sequence',
        'clear \t\t-> clear the terminal',
        'help \t\t\t-> show this help',
    ]
    for command in commands:
        print(f'\t- {command}')

def prompt_user():
    print('')
    command = input('>>> ')
    if not command:
        return[]
    else:
        return command.split()

def print_list():
    global files
    if files:
        print('You added the following files:')
        print('')
        for file in files:
            print(file)
    else:
        print('No files added yet')

#Grid aus einer .csv-Datei einlesen
def grid_read(file):
    grid = []
    with open(r'grids/' + file + '.csv') as f:
        content = csv.reader(f)
        for row in content:
            #kleine list comprehension um die Values als int zu speichern
            grid.append([int(i) for i in row])
    return grid

#Das aktuelle Grid "beautified" ausgeben
def grid_print(file):
    grid = grid_read(file)
    print_horizontal_separator = lambda: print('+' + '-------+' * 3)
    print_horizontal_separator()

    for y, row in enumerate(grid, 1):
        row_temp = '| '
        for x, value in enumerate(row, 1):
            separator = ''
            if x % 3 == 0 and x < 8:
                separator = ' | '
            else:
                separator = ' '
            row_temp += str(value) + separator
        row_temp += '|'
        print(row_temp)
        if y % 3 == 0:
            print_horizontal_separator()

def ls():
    print('The following grids are available in grids/:')
    print('')
    files = os.listdir('grids/')
    for file in files:
        print(file)

if __name__ == '__main__':

    solved_grids = []
    exceptions = {}
    files = []

    clear_terminal()
    greet()
    print_help()

    while True:
        command = prompt_user()
        if command == []:
            continue
        elif command == ['clear']:
            clear_terminal()
            continue
        elif command == ['list']:
            ls()
            continue
        elif command == ['quit']:
            clear_terminal()
            sys.exit()
        elif command == ['help']:
            print_help()
            continue
        elif command == ['files']:
            print_list()
            continue
        elif len(command) == 2:
            if command[0] == 'add':
                file = command[1]
                if file in files:
                    print('Error: file already in files')
                    continue
                elif not os.path.exists('grids/' + file + '.csv'):
                    print('Error: file does not exist')
                    continue
                else:
                    print(f'Adding {file}.csv to files...')
                    files.append(file)
                    continue
            elif command[0] == 'print':
                    file = command[1]
                    if not os.path.exists('grids/' + file + '.csv'):
                        print('Error: file does not exist')
                        continue
                    else:
                        grid_print(file)
                        continue
            elif command[0] == 'remove':
                if len(command) == 2:
                    file = command[1]
                    if file in files:
                        files.remove(file)
                        print(f'Removing {file}.csv from files...')
                        continue
                    else:
                        print(f'Error: {file}.csv is not in files.')
                        files.append(file)
                        continue
            else:
                pass
        elif command == ['solve']:
            if not files:
                print('Add some grids first...')
                continue
            confirmation = input('Start the test sequence? [y/n]... ')
            if confirmation == 'y':
                break
            elif confirmation == 'n':
                continue
            else:
                print('Error: please enter a valid command!')
                continue
        else:
            print('Error: please enter a valid command!')


    for file in files:
        clear_terminal()
        print(f'Getting ready for: {file}...')
        time.sleep(3)
        try:
            s = Sudoku(file, recording = True)
            s.solve()
            if s.solved == True:
                solved_grids.append(file)
            if s.exceptions:
                exceptions[file] = s.exceptions

            h = Heatmap(file)
            h.plot_data()
        except:
            pass

    clear_terminal()
    print('Sequence completed!')
    print(f'\nThe following Sudokus could be solved:')
    print('')
    for grid in solved_grids:
        print(f'\t- {grid}')
    num_exceptions = len(exceptions.keys())
    print(f'\nThere has/have been {num_exceptions} exception(s).')
    print('')

    for key, message in exceptions.items():
        print(f'\t- {key}: {message}')
    time.sleep(5)
else:
    clear_terminal()
    print('Error: no files specified.')
