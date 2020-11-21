import os

def grid_import(file):
    filename = r'grids/' + file
    output = []
    with open(filename) as f:
        for line in f:
            output.append([int(i) for i in line.strip().split()])
    return output

def grid_print(grid):
    separate = lambda: print('+' + 3 * '-------+')
    separate()
    for y, row in enumerate(grid,1):
        row_temp = '| '
        for x, value in enumerate(row,1):
            if x % 3 == 0:
                row_temp += str(value) + ' | '
            else:
                row_temp += str(value) + ' '
        print(row_temp)
        if y % 3 == 0:
            separate()

def create_coordinates():
    pass

grid = grid_import('grid_wikipedia.txt')


os.system('clear')
grid_print(grid)

