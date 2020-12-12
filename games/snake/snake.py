import random
import time
import sys
import os
import copy
import csv

class Snake():
    def __init__(self, height, width, attempt, **kwargs):
        self.kwargs = kwargs
        self.width = width
        self.height = height
        self.world = []
        self.buffer = []
        self.head = ()
        self.segments = []
        self.snacks = []
        self.moves = 0
        self.terminated = False
        self.cause = ''
        self.log = {}
        self.attempt = attempt
        self.verbose = False
        try:
            self.verbose = self.kwargs['verbose']
        except:
            pass

    def write_buffer(self):
        self.buffer = copy.deepcopy(self.world)

        for snack in self.snacks:
            self.buffer[snack[0]][snack[1]] = 's'

        if self.head:
            self.buffer[self.head[0]][self.head[1]] = '@'

        for segment in self.segments:
            self.buffer[segment[0]][segment[1]] = 'o'

    def print_world(self):
        self.write_buffer()

        for row in self.buffer:
            print(''.join(row))

    def move(self):
        directions_base = {
            'N': (-1,0),
            'E': (0,1),
            'S': (1,0),
            'W': (0,-1),
        }

        directions = list(directions_base)
        random.shuffle(directions)
        while directions:
            direction = directions.pop()
            self.write_buffer()
            current_y = self.head[0]
            current_x = self.head[1]
            new_y = self.head[0] + directions_base[direction][0]
            new_x = self.head[1] + directions_base[direction][1]
            destination = self.buffer[new_y][new_x]

            if destination in ('#', 'o'):
                continue
            elif destination == 's':
                self.segments.append((current_y, current_x))
                self.head = (new_y, new_x)
                self.snacks.pop(0)
                self.spawn_snack()
                self.moves += 1
                break
            elif destination == ' ':
                self.head = (new_y, new_x)
                if self.segments:
                    self.segments.pop(0)
                    self.segments.append((current_y, current_x))
                self.moves += 1
                break
        else:
            self.terminated = True

    def clear_terminal(self):
        os.system('clear')

    def spawn_head(self):
        while True:
            self.write_buffer()
            y = random.randint(0, self.height -1)
            x = random.randint(0, self.width - 1)
            self.head = (y, x)
            if self.buffer[self.head[0]][self.head[1]] == ' ':
                break

    def spawn_snack(self):
        while True:
            self.write_buffer()
            y = random.randint(0, self.height -1)
            x = random.randint(0, self.width - 1)
            pos = (y, x)
            if self.buffer[pos[0]][pos[1]] == ' ':
                self.snacks.append(pos)
                break

    def create_world(self):
        #initialize list for world
        self.world = [[] for i in range(self.height)]
        for row in self.world:
            for i in range(self.width):
                row.append(' ')
        #create borders
        for y, row in enumerate(self.world):
            for x, column in enumerate(row):
                if y in {0, len(self.world)-1}:
                    self.world[y][x] = '#'
                if x in {0, len(self.world[0])-1}:
                         self.world[y][x] = '#'
    def initialize(self):
        self.create_world()
        self.spawn_head()
        self.spawn_snack()

    def main(self):
        s.initialize()
        while True:
            try:
                s.move()
                if s.verbose:
                    s.clear_terminal()
                    s.print_world()
                    print(f'moves: {s.moves}')
                if s.terminated == True:
                    self.log['moves'] = self.moves
                    self.log['cause'] = self.cause
                    s.clear_terminal()
                    s.print_world()
                    print(s.moves)
                    print(s.attempt)
                    break

            except KeyboardInterrupt:
                sys.exit()

    def log_data(self):
        with open('data/attempt' + str(self.attempt) + '.json', 'w') as f:
            json.dump(self.log,f)


if __name__ == '__main__':
    f = open('data/log.csv', 'a')
    writer = csv.writer(f)
    for attempt in range(1000):
        log_attempt = {}
        s = Snake(10,10, attempt, verbose = False)
        s.main()
        writer.writerow([s.attempt, s.height, s.width, s.moves, len(s.segments)])

    f.close
