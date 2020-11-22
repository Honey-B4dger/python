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

    while grid_2_check:
        row_2_check = grid_2_check.pop(0)
        for symbol in ['O', 'X',]:
            if row_2_check.count(symbol):
                print('4 in a row!')
                return False
    print('grid is clear')
    return True

grid = [
    ['O', 'X', 'O', 'X', 'O', 'X', 'O', ],
    ['X', 'X', 'X', 'O', 'X', 'O', 'X',],
    ['O', 'X', 'O', 'X', 'O', 'X', 'O', ],
    ['X', 'O', 'X', 'O', 'X', 'O', 'X',],
    ['O', 'X', 'O', 'O', 'O', 'X', 'O', ],
    ['X', 'O', 'X', 'O', 'X', 'O', 'X',],
]

#for line in grid:
#    print(line)
#
#for line in d_slicer(grid, 'nw'):
#    print(line)
#
#for line in d_slicer(grid, 'ne'):
#    print(line)

for line in all_slices(grid):
    print(line)

check_grid(grid)
