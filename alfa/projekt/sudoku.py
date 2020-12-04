import csv
import os
import sys

class Sudoku():
    """ Diese Klasse dient zum Lösen eines Sudokus.
    Es kann ein Feld eingelesen werden und - falls möglich - mit Hilfe eines
    Backtracking-Algorithmus gelöst werden.
    """

    def __init__(self, file, **kwargs):
        self.file = file
        self.kwargs = kwargs
        self.recording = False
        self.grid = []
        self.solved = False
        self.relevant_vertices = []
        self.coordinates = []
        self.cursor = 0
        self.iterations = 0
        try:
            self.recording = kwargs['recording']
        except:
            pass


#        if 'recording' in self.kwargs.keys():
#            self.recording = kwargs['recording']
#            self.log = []

    #Grid aus einer .csv-Datei einlesen
    def grid_read(self):
        with open(r'grids/' + self.file) as f:
            content = csv.reader(f)
            for row in content:
                #kleine list comprehension um die Values als int zu speichern
                self.grid.append([int(i) for i in row])

    #Das aktuelle Grid beautified ausgeben
    def grid_print(self):
        print_horizontal_separator = lambda: print('+' + '-------+' * 3)
        print_horizontal_separator()

        for y, row in enumerate(self.grid, 1):
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

    def get_relevant_vertices(self):
        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                if value == 0:
                    self.relevant_vertices.append((y,x))

    #den Sektor eines Koordinaten-Tupels bestimmen
    def get_sector(self, coords):
        y, x = coords
        return x // 3 + y //3 * 3

    def check_cursor(self):
        result = True
        #list mir 3 lists erzeugen
        slices = [[] for i in range(3)]
        coordinates = self.relevant_vertices[self.cursor]

        cursor_y, cursor_x = coordinates
        cursor_value = self.grid[cursor_y][cursor_x]
        cursor_sector = self.get_sector(coordinates)

        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                if y == cursor_y:
                    slices[0].append(value)
                if x == cursor_x:
                    slices[1].append(value)
                if self.get_sector((y,x)) == cursor_sector:
                    slices[2].append(value)

        for slice_ in slices:
            if slice_.count(cursor_value) > 1:
                result = False

        if self.cursor == (len(self.relevant_vertices) -1) and result == True:
            self.solved = True

        return result

    def step(self):
        cursor_y, cursor_x = self.relevant_vertices[self.cursor]
        value = self.grid[cursor_y][cursor_x]
        if value < 9:
            self.grid[cursor_y][cursor_x] +=1
            if self.check_cursor():
                self.cursor += 1
        else:
            self.backtrack()

    def backtrack(self):
        y, x = self.relevant_vertices[self.cursor]
        self.grid[y][x] = 0
        self.cursor -= 1

    def writer_initialize(self):
        filename = s.file.split('.')[0] + '.log'
        f = open(filename, 'w')
        s.log = csv.writer(f)
        header = ['iteration', 'row', 'column', 'value']
        s.log.writerow(header)


    def initialize(self):
        self.grid_read()
        self.get_relevant_vertices()
        if s.recording == True:
            self.writer_initialize()

    def clear_terminal(self):
        os.system('clear')



if __name__ == '__main__':
    s = Sudoku('wikipedia.csv', recording = True)
    s.initialize()


    while True:
        try:
            if s.recording == True:
                log_y, log_x = s.relevant_vertices[s.cursor]
                line = []

                for el in[s.iterations, log_y, log_x, s.grid[log_y][log_x]]:
                    line.append(el)
                s.log.writerow(line)

            s.step()
            s.iterations += 1
            if s.iterations%1000 == 0:
                s.clear_terminal()
                s.grid_print()
                print(f'iterations: {s.iterations}')

            if s.solved == True:
                s.clear_terminal()
                print(f'solution found after {s.iterations} iterations!')
                s.grid_print()
                break

        except IndexError:
            print('Sorry, IndexError')
            break
        except KeyboardInterrupt:
            sys.exit()
