import re
import os

class Sudoku():
    def __init__(self, file):
        self.file = file
        self.solved = False
        self.presets = []
        self.iterations = 0
        self.coordinates = []
        self.vertices = []
        self.quadrants = []
        self.subjects = []
        self.cursor = -1
        self.stay = False

    def check_solution(self):
        correct = True

        for vertex in range(81):

            current_value = self.vertices[vertex]['current_value']

            row = self.vertices[vertex]['coords'][0]
            col = self.vertices[vertex]['coords'][1]
            quadrant = self.vertices[vertex]['quadrant']

            h_slice = []
            v_slice = []
            q_slice = []

            for i in range(81):
                if self.vertices[i]['coords'][0] == row:
                    h_slice.append(str(self.vertices[i]['current_value']))
                if self.vertices[i]['coords'][1] == col:
                    v_slice.append(str(self.vertices[i]['current_value']))
                if self.vertices[i]['quadrant'] == quadrant:
                    q_slice.append(str(self.vertices[i]['current_value']))

            slices = []
            slices.append(''.join(h_slice))
            slices.append(''.join(v_slice))
            slices.append(''.join(q_slice))

            for digit in range(1,9):
                for slice_ in slices:
                    result = re.findall(str(digit), slice_)
                    #print(digit, slice_, len(result))
                    #print(result)
                    if len(result) > 1:
                        correct = False
                        #print(vertex, digit)
        #print(correct)
        return correct

    def create_coordinates(self):
        for row in range(9):
            for column in range(9):
                self.coordinates.append((row, column))

    def create_vertices(self):
        for i in range(81):
            dict = {}
            dict.update({'index': i})
            dict.update({'coords' : self.coordinates[i]})

            if self.presets[i] == '0':
                preset = False
            else:
                preset = True

            dict.update({'guess': int()})
            dict.update({'preset': preset})
            dict.update({'quadrant': int()})
            dict.update({'preset_value': self.presets[i]})
            dict.update({'current_value': int(self.presets[i])})

            self.vertices.append(dict)

    def determine_subjects(self):

        for index, value in enumerate(self.presets):
            if value == '0':
                self.subjects.append(index)
        #print(self.subjects)



    def read_presets(self):
        with open(self.file, 'r') as f:
            content = f.read()
            for char in content:
                if char in [str(i) for i in range(10)]:
                    self.presets.append(char)

    def set_quadrants(self):
        for i in range(81):
            row = self.vertices[i]['coords'][0]
            col = self.vertices[i]['coords'][1]

            if 0 <= row < 3 and  0 <= col < 3:
                self.vertices[i]['quadrant'] = 0
            elif 0 <= row < 3 and  3 <= col < 6:
                self.vertices[i]['quadrant'] = 1
            elif 0 <= row < 3 and  6 <= col < 9:
                self.vertices[i]['quadrant'] = 2

            if 3 <= row < 6 and  0 <= col < 3:
                self.vertices[i]['quadrant'] = 3
            elif 3 <= row < 6 and  3 <= col < 6:
                self.vertices[i]['quadrant'] = 4
            elif 3 <= row < 6 and  6 <= col < 9:
                self.vertices[i]['quadrant'] = 5

            if 6 <= row < 9 and  0 <= col < 3:
                self.vertices[i]['quadrant'] = 6
            elif 6 <= row < 9 and  3 <= col < 6:
                self.vertices[i]['quadrant'] = 7
            elif 6 <= row < 9 and  6 <= col < 9:
                self.vertices[i]['quadrant'] = 8

    def initialize_cursor(self):
        self.cursor = 0
        while self.get_preset(self.cursor):
            self.cursor += 1
        self.cursor_initial = self.cursor

    def print_values(self, key):
        values = []
        for i in range(81):
            values.append(self.vertices[i][key])

        for i in range(9):
            print(values[i * 9: i * 9 + 9])
            print('')

    def initialize(self):
        self.create_coordinates()
        self.read_presets()
        self.create_vertices()
        self.set_quadrants()
        self.determine_subjects()
        self.initialize_cursor()

    def get_value(self, vertex):
        return self.vertices[vertex]['current_value']

    def set_value(self, vertex, value):
        self.vertices[vertex].update({'current_value': value})

    def get_preset(self, vertex):
        return self.vertices[vertex]['preset']

    def print_status(self):
        self.print_values('current_value')
        print(f'solution status: {self.check_solution()}')
        print(f'cursor: {self.cursor}')
        print(f'iterations: {self.iterations}')

    def increment(self):
        value = self.get_value(self.cursor)
        self.set_value(self.cursor, value + 1)

    def move_forward(self):
        self.cursor += 1
        if self.get_preset(self.cursor):
            self.move_forward()

    def move_backward(self):
        self.cursor -= 1
        if self.cursor < self.cursor_initial:
            self.cursor = self.cursor_initial
        elif self.get_preset(self.cursor):
            self.move_backward()
        else:
            pass

    def cursor_value(self):
        return self.get_value(self.cursor)

def main():
    s = Sudoku(r'grids/grid_wikipedia.txt')
    s.initialize()
    print('foo')


    while True and s.cursor in range(0,81):

        #os.system('clear')

        print('vvvvvvvvvv')
        print(f'cursor: {s.cursor}')
        s.print_values('current_value')

        s.increment()
        solution = s.check_solution()
        value = s.cursor_value()

        if value < 9 and not solution:
            print('value < 9, no solution')
            continue
        elif value >= 9 and not solution:
            print('value == 9, no solution')
            s.set_value(s.cursor, 0)
            print('moving backward')
            s.move_backward()
        elif value <= 9 and solution:
            print('value < 9, solution')
            s.move_forward()
        else:
            print('pass')
            pass




        print(f'cursor : {s.cursor}')
        s.print_values('current_value')
        #s.print_status()
        print('^^^^^^^^^^')

        if s.iterations > 10:
            break
        elif s.cursor > 80 and s.checkSolution():
            print('solution found!')
            break
        else:
            pass


if __name__ == "__main__":
    main()
