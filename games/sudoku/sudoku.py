field = []
coordinates = []

def init_field():
    global field
    global coordinates
    for row in range(9):
        row_temp = []
        for column in range(9):
            index = 10 * row + column
            row_temp.append(index)
            coordinates.append((row, column))
        field.append(row_temp)


def import_field(file):
    with open(file, 'r') as f:
        content = f.readlines()
        output = []
        for line in content:
            output.append(line.strip().split())
        return(output)

def print_(array):
    for line in array:
        print(line)

if __name__ == '__main__':
    init_field()
#    print_(field)
#    print_(coordinates)
    imported_field = import_field(r'grids/grid_wikipedia.txt')
    print_(imported_field)
