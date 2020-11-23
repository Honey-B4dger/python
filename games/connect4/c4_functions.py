import random

def d_slicer(grid_input, direction):
    result_temp = []
    l = list(range(len(grid_input[0])))
    r = l[:]
    r.reverse()
    if direction == 'nw':
        pass
    if direction == 'ne':
        l.reverse()
        r.reverse()

    for row in grid_input:
        row_temp = ['0' for i in range(l.pop())]
        row_temp += row
        row_temp += ['0' for i in range(r.pop())]
        result_temp.append(row_temp)

    result = []
    for x, columns in enumerate(result_temp[0]):
        result.append([row[x] for row in result_temp])

    return result

def all_slices(grid):
    result = []
    result += d_slicer(grid, 'nw')
    result += d_slicer(grid, 'ne')
    for row in grid:
        result.append(row)

    for column in  range(3):
        result.append([row[column] for row in grid])

    return result

def check_grid(grid):

    grid_2_check = all_slices(grid)
    for y, row in enumerate(grid_2_check):
        print(f'Zeile: {y} {row}')

    print('')

    for y, row in enumerate(grid_2_check):
        for symbol in ['O', 'X']:
            occurrences = 0
            for column in row:
                if column == symbol:
                    occurrences += 1
                else:
                    occurrences = 0
                if occurrences >= 4:
                    #print('4 in einer Reihe')
                    #print(f'in Reihe {y}')
                    return True
    #print('Keine 4 in einer Reihe')
    return False

def topped_off(grid):
    #print(f'topped_off:')
    #print(grid[0])
    if ' ' in grid[0]:
        #print('leere Zelle gefunden')
        return False
    else:
        return True

if __name__ == '__main__':
    grid = [
        ['O', 'X', 'O', 'X', 'O', 'X', 'O', ],
        ['X', 'X', 'X', 'O', 'X', 'O', 'X', ],
        ['O', 'X', 'O', 'X', 'O', 'X', 'O', ],
        ['X', 'O', 'X', 'O', 'X', 'O', 'X', ],
        ['O', 'X', 'O', 'O', 'O', 'X', 'O', ],
        ['X', 'O', 'X', 'O', 'X', 'O', 'X', ],
    ]

    for line in grid:
        random.shuffle(line)

    #for line in grid:
    #    print(line)
    #
    #for line in d_slicer(grid, 'nw'):
    #    print(line)
    #
    #for line in d_slicer(grid, 'ne'):
    #    print(line)

    for line in grid:
        print(line)

#    for line in all_slices(grid):
        #print(line)

    print('=======')

    check_grid(grid)
