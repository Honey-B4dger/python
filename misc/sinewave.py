import math
import os

matrix = []
phase = 0

width, height = 90, 30
amplitude = height

def write_element(row, column):
    global width, height

    arg = column/width * 2 * math.pi
    y_max = abs(height * math.cos(arg + phase))

    if row >= y_max:
        return 'O'
    else:
        return ' '

def write_matrix():
    global matrix
    for row in range(height):
        row_temp = []
        for column in range(width):
            row_temp.append(write_element(row, column))
        matrix.append(row_temp)


def main():

    write_matrix()

    for line in matrix:
        print(''.join(line))

if __name__ == '__main__':
    main()
