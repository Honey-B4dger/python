import re
import os
import time

file_name = r'grids/grid_wikipedia.txt'
field = []
imported_field = []
coordinates = []
relevants = []
cursor = 0
iterations = 0

def init_field():
    for row in range(9):
        row_temp = []
        for column in range(9):
            row_temp.append([])
            coordinates.append((row, column))
        field.append(row_temp)

def progress_bar():
    progress = int(cursor / len(relevants) * 50)
    remaining = 50 - progress
    output = '[' + progress * '#' + remaining * '.' + ']'

    return(output)

def import_field(file):
    global imported_field
    with open(file, 'r') as f:
        for line in f:
            imported_field.append([int(i) for i in line.strip().split()])

def get_quadrant(coords):
    row = coords[0]
    column = coords[1]

    return column//3 + row//3 * 3

def create_relevants():
    global imported_field
    global relevants
    for y, row in enumerate(imported_field):
        for x, column in enumerate(row):
            if column == 0:
                relevants.append((y, x))

def create_slices(coords):
    row, column = coords
    slices = []
    # horizontal
    slices.append(imported_field[row])

    # vertical
    temp = []
    for row in imported_field:
        #print(row)
        temp.append(row[column])
    slices.append(temp)

    # quadrant
    temp = []
    quadrant = get_quadrant(coords)
    for y, row in enumerate(imported_field):
        for x, column in enumerate(row):
            if get_quadrant((y,x)) == quadrant:
                temp.append(column)
    slices.append(temp)

    return slices

def print_():
    global imported_field
    separate = lambda: print('+' + 3 * '-------+')
    separate()
    for y, row in enumerate(imported_field,1):
        row_temp = '| '
        for x, value in enumerate(row,1):
            if x % 3 == 0:
                row_temp += str(value) + ' | '
            else:
                row_temp += str(value) + ' '
        print(row_temp)
        if y % 3 == 0:
            separate()


def initialize():
    global start_time
    init_field()
    import_field(file_name)
    create_relevants()
    start_time = time.time()

def validate():
    global cursor
    global imported_field
    coords = relevants[cursor]
    slices = []
    value = imported_field[coords[0]][coords[1]]
    valid = True
    if value != 0:

        slices = create_slices(coords)

        for line in slices:
            if line.count(value) > 1:
                valid = False

    return valid

def get_value():
    global cursor
    global imported_field
    row, column = relevants[cursor]
    value = imported_field[row][column]
    return value

def increment():
    global cursor
    global imported_field
    row, column = relevants[cursor]
    value = imported_field[row][column]
    imported_field[row][column] += 1

def backtrack():
    global cursor
    global imported_field
    row, column = relevants[cursor]
    imported_field[row][column] = 0
    cursor -= 1

if __name__ == '__main__':
    initialize()
    print_()

    while True:
        try:
            coords = relevants[cursor]
            value = get_value()

            if value in range(9):
                increment()
                valid = validate()
                if valid and cursor != len(relevants) - 1:
                    cursor += 1
                elif valid and cursor == len(relevants) -1:
                    os.system('clear')
                    print('sudoku solved :)')
                    print('')
                    print_()
                    print(f'iterations: {iterations}')
                    elapsed = round(time.time() - start_time, 1)
                    print(f'elapsed time: {elapsed} s')
                    break
                else:
                    pass

            else:
                backtrack()
            iterations += 1

            if iterations%1000 == 0:
                os.system('clear')
                print('\n\n')
                print_()
                print(f'iterations: {iterations}')
                print('\n Progress:')
                print(progress_bar())

        except (IndexError, KeyboardInterrupt):
            print(f'no solution after {iterations} iterations')
            print('solving interrupted')
            break

        finally:
            pass





