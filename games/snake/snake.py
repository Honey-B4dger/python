import random
import time
import sys
import os
import copy
import csv

class Snake():
    def __init__(self, height, width, **kwargs):
        self.kwargs = kwargs
        self.dimensions = (width, height)
        self.world = []
        self.buffer = []
        self.head = ()
        self.segments = []
        self.snacks = []
        self.moves = 0
        self.terminated = False
        self.cause = ''
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

    def get_direction(self):
        directions_pool = {
            'N': (-1,0),
            'E': (0,1),
            'S': (1,0),
            'W': (0,-1),
        }

        directions = list(directions_pool)
        random.shuffle(directions)


    def get_destination(self):
        pass

    def check_destination(self):
        pass

    def eat_snack(self, foo):
        print('eating snack...')
        time.sleep(1)

    def move(self):
        directions_pool = {
            'N': (-1,0),
            'E': (0,1),
            'S': (1,0),
            'W': (0,-1),
        }

        directions = list(directions_pool)
        random.shuffle(directions)

        while directions:
            direction = directions.pop()
            self.write_buffer()
            new_y = self.head[0] + directions_pool[direction][0]
            new_x = self.head[1] + directions_pool[direction][1]
            destination = self.buffer[new_y][new_x]

            if destination in ('#', 'o'):
                continue
            elif destination == 's':
                self.eat_snack()
                self.segments.append((self.head[0], self.head[1]))
                self.head = (new_y, new_x)
                self.snacks.pop(0)
                self.spawn_snack()
                self.moves += 1
                break
            elif destination == ' ':
                self.head = (new_y, new_x)
                if self.segments:
                    self.segments.pop(0)
                    self.segments.append((self.head[0], self.head[1]))
                self.moves += 1
                break
        else:
            self.terminated = True

    def clear_terminal(self):
        os.system('clear')

    def spawn_head(self):
        while True:
            self.write_buffer()
            y = random.randint(0, self.dimensions[0] -1)
            x = random.randint(0, self.dimensions[1] - 1)
            self.head = (y, x)
            if self.buffer[self.head[0]][self.head[1]] == ' ':
                break

    def spawn_snack(self):
        while True:
            self.write_buffer()
            y = random.randint(0, self.dimensions[0] -1)
            x = random.randint(0, self.dimensions[1] - 1)
            pos = (y, x)
            if self.buffer[pos[0]][pos[1]] == ' ':
                self.snacks.append(pos)
                break

    def eat_snack(self):
        pass

    def create_world(self):
        #initialize list for world
        self.world = [[] for i in range(self.dimensions[0])]
        for row in self.world:
            for i in range(self.dimensions[1]):
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

    def print_setup(self):
        print(f'height x width: {self.dimensions[0]} x {self.dimensions[1]}')

    def main(self):
        self.initialize()
        while True:
            try:
                self.move()
                if self.verbose:
                    self.clear_terminal()
                    self.print_world()
                    print(f'moves: {s.moves}')
                if self.terminated == True:
                    self.clear_terminal()
                    self.print_world()
                    self.print_setup()
                    print(f'Moves: {self.moves}')
                    break

            except KeyboardInterrupt:
                sys.exit()
#        else:
#            self.print_setup()

main()
