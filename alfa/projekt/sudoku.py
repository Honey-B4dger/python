import csv
import os
import sys
import json
import time
from heatmap import Heatmap

class Sudoku():
    """ Diese Klasse dient zum Lösen eines Sudokus.
    Es kann ein Gitter eingelesen werden und - falls eine Loesung existiert -
    mit Hilfe eines Backtracking-Algorithmus gelöst werden.

    Mit dem Keyword-Argument "recording = True" können Daten aufgezeichnet werden
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
        self.solution = []
        self.exceptions = []
        #pruefen, ob eine Datenaufzeichnung per kwarg gewünscht ist
        try:
            self.recording = kwargs['recording']
        except:
            pass
        else:
            self.data = {}

    #Grid aus einer .csv-Datei einlesen
    def grid_read(self):
        with open(r'grids/' + self.file + '.csv') as f:
            content = csv.reader(f)
            for row in content:
                #kleine list comprehension um die Values als int zu speichern
                self.grid.append([int(i) for i in row])

    #Das aktuelle Grid "beautified" ausgeben
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
        #list fuer 3 Slices (hor, vert, quadrant)rzeugen
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

        #pruefen, ob der Wert am Cursor mehr als 1 Mal pro Slice vorkommt
        for slice_ in slices:
            if slice_.count(cursor_value) > 1:
                result = False

        #wenn im letzten Feld result = True, dann ist das Raetsel geloest
        if self.cursor == (len(self.relevant_vertices) -1) and result == True:
            self.solution = self.grid
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

    def recorder_initialize(self):
        filename = 'data/' + self.file + '.log'
        f = open(filename, 'w')
        self.log = csv.writer(f)
        header = ['iteration', 'row', 'column', 'value']
        self.log.writerow(header)

        self.frequencies = [[] for i in range(9)]
        for row in self.frequencies:
            for i in range(9):
                row.append(0)

    def initialize(self):
        self.grid_read()
        self.get_relevant_vertices()
        if self.recording == True:
            self.recorder_initialize()
            self.t_start = time.time()

    @staticmethod
    def clear_terminal():
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

    #ggf. die Loesung as .csv schreiben
    #falls gewuenscht, die frequencies as .json schreiben
    def write_final_data(self):
        if self.solved == True:
            with open('data/' + self.file + '_solution.csv', 'w') as f:
                for row in self.solution:
                    f.write(', '.join([str(i) for i in row]) + '\n')

        if self.recording == True:
            self.data['frequencies'] = self.frequencies
            self.data['iterations'] = self.iterations
            self.data['time'] = round(time.time() - self.t_start, 1)
            with open('data/' + self.file + '_data.json', 'w') as f:
                json.dump(self.data, f, indent = 4)
            print('\nOutput data has been written.')
        else:
            print('\nNo data has been recorded.')

    def solve(self):
        self.initialize()

        while True:
            try:
                #ggf. Iteration, Zeile, Spalte und Wert loggen 
                if self.recording == True:
                    log_y, log_x = self.relevant_vertices[self.cursor]
                    self.frequencies[log_y][log_x] += 1
                    line = []

                    for el in[self.iterations, log_y, log_x, self.grid[log_y][log_x]]:
                        line.append(el)
                    self.log.writerow(line)

                #einen schritt versuchen, ggf. backtracken
                self.step()
                self.iterations += 1

                #alle 1.000 Zyklen den aktuellen Status in der Konsole ausgeben
                if self.iterations%5000 == 0:
                    self.clear_terminal()
                    print(f'Solving "{self.file}"')
                    self.grid_print()
                    print(f'iterations: {self.iterations}')

                #falls Raetsel geloest, das Progamm beenden und Daten schreiben
                if self.solved == True:
                    self.clear_terminal()
                    print(f'Sudoku {self.file} has been solved!')
                    self.grid_print()
                    print(f'solution found after {self.iterations} iterations!')
                    self.write_final_data()
                    time.sleep(2)
                    break

            #IndexError bedeutet, dass keine Loesung gefunden werden konnte
            except Exception as e:
                self.exceptions.append(e)
                print(e)
                break
            #bei ctrl+D das Programm beenden
            except KeyboardInterrupt:
                sys.exit()
