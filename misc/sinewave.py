import math as m
import os
import time
import sys

matrix = []

width, height = 80, 30
wl = 40
amp = height / 2
phase = 0
f = 0

def matrix_init():
    for row in range(height):
        matrix.append([' ' for i in range(width)])

def matrix_fill():
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            y_limit = amp + amp * f * m.sin(2 * m.pi * (x/wl + phase/360))
            if y >= y_limit:
                matrix[y][x] = 'O'
            else:
                matrix[y][x] = ' '

def matrix_print():
    for line in matrix:
        print(''.join(line))

if __name__ == '__main__':
    matrix_init()
    try:
        while True:
            os.system('clear')
            matrix_fill()

            matrix_print()

            f = m.sin(2 * m.pi * phase/360)

            phase += 10
            if phase > 360:
                phase = 0

            time.sleep(.1)
    except KeyboardInterrupt:
        sys.exit()
