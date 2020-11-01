class Maze():
    def __init__(self, file):
        self.file = file
        self.map = []
        self.cursor = ()
        self.seen = []
        self.buffer = []
        self.directions = {}

    def conti(self):
        input('Press return to continue.')

    def initialize_map(self):
        with open(self.file, 'r') as f:
            content = f.read().splitlines()
            for line in content:
                tmp = []
                for char in line:
                    tmp.append(char)
                self.map.append(tmp)
        self.height = len(self.map)
        self.width = len(self.map[1])

    def print_map(self):
        self.buffer = self.map
        self.buffer[self.cursor[0]][self.cursor[1]] = r'@'
        for row, line in enumerate(self.seen):
            for column, value in enumerate(line):
                if value == 'O':
                    self.buffer[row][column] = 'O'
        for line in self.buffer:
            print(''.join(line))

    def initialize_cursor(self):
        for row, line in enumerate(self.map):
            if 'S' in line:
                self.cursor = (row, line.index('S'))

    def initialize_buffer_seen(self):
        for row in range(self.height):
            tmp = []
            for column in range(self.width):
                tmp.append(' ')
            self.buffer.append(tmp)
            self.seen.append(tmp)



    def initialize(self):
        self.initialize_map()
        self.initialize_buffer_seen()
        self.initialize_cursor()

        self.directions.update({'up': [-1, -1]})
        self.directions.update({'right': [0, 1]})
        self.directions.update({'down': [1, 0]})
        self.directions.update({'left': [0, -1]})
