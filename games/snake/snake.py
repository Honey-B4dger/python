import random
import time
import sys
import os
import copy
import csv

class Snake():
    def __init__(self, height, width, **kwargs):
        self.kwargs = kwargs
        self.dimensions = (height, width)
        self.world = []
        self.buffer = []
        self.head = ()
        self.segments = []
        self.snacks = []
        self.moves = 0
        self.status = 'okay'
        self.energy = 50
        self.snack_increment = 100
        self.heading = 'N'
        self.directions = {
            'N': (-1,0),
            'E': (0,1),
            'S': (1,0),
            'W': (0,-1),
        }

        if 'v' in self.kwargs:
            self.verbose = self.kwargs['v']
        else:
            self.verbose = ''
        if 'starve' in self.kwargs:

            self.starvation = self.kwargs['starve']
        else:
            self.starvation = False

#-------------------------------------------------------------------------------
    def write_buffer(self):
        self.buffer = copy.deepcopy(self.world)

        for snack in self.snacks:
            self.buffer[snack[0]][snack[1]] = 's'

        if self.head:
            self.buffer[self.head[0]][self.head[1]] = '@'

        for segment in self.segments:
            self.buffer[segment[0]][segment[1]] = 'o'

    def print_world(self):

        for row in self.buffer:
            print(''.join(row))

    #random walk
    def set_directions(self):
        #tupel aus dictionary abgreifen
        directions = list(self.directions.keys())
        random.shuffle(directions)
        return directions

    def get_surroundings(self):
        surroundings = {}
        keys = ['N', 'E', 'S', 'W',]
        deltas = [(-1,0), (0,1), (1,0), (0,-1)]
        for index, delta in enumerate(deltas):
            y = self.head[0] + delta[0]
            x = self.head[1] + delta[1]
            surroundings[keys[index]] = self.buffer[y][x]
        return surroundings

    def check_surroundings(self):
        valid = False
        surroundings = list(self.get_surroundings().values())
        necessaries = (' ', 's')
        for necessary in necessaries:
            if necessary in surroundings:
                valid = True
        return valid

    def eat_snack(self, new_y, new_x):
        self.segments.append((self.head[0], self.head[1]))
        #self.head = (new_y, new_x)
        self.snacks.pop(0)
        if self.starvation:
            self.energy += self.snack_increment

    def move_snake(self, new_y, new_x):
        if self.segments:
            self.segments.pop(0)
            self.segments.append((self.head[0], self.head[1]))
        self.head = (new_y, new_x)
        self.moves += 1
        if self.starvation:
            self.energy -= 1

    def get_destination_symbol(self, direction):
        new_y, new_x = self.get_destination_coordinates(direction)
        return self.buffer[new_y][new_x]

    def get_destination_coordinates(self, direction):
        new_y = self.head[0] + self.directions[direction][0]
        new_x = self.head[1] + self.directions[direction][1]
        return (new_y, new_x)

#------------------------------------------------------------------------------
    def step(self):

        directions = self.set_directions()

        while directions:
            direction = directions.pop(0)
            destination = self.get_destination_symbol(direction)
            new_y, new_x = self.get_destination_coordinates(direction)

            if destination in ('#', 'o'):
                continue
            elif destination == 's':
                self.eat_snack(new_y, new_x)
                self.spawn_snack(1)
                self.move_snake(new_y, new_x)
                directions = []
                break
            elif destination == ' ':
                self.move_snake(new_y, new_x)
                directions = []
                break

#-------------------------------------------------------------------------------
    def check_status(self):
        result = True

        if len(self.segments) < self.moves // 1000:
            self.status = 'stuck'
            result = False
        if not self.check_surroundings():
            self.status = 'out_of_moves'
            result = False

        if self.energy <= 0:
            self.status = 'starved'
            result = False
        return result

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

    def spawn_snack(self, amount):
        if len(self.snacks) >= amount:
            pass
        else:
            for i in range(amount - len(self.snacks)):
                while True:
                    self.write_buffer()
                    y = random.randint(0, self.dimensions[0] -1)
                    x = random.randint(0, self.dimensions[1] - 1)
                    pos = (y, x)
                    if self.buffer[pos[0]][pos[1]] == ' ':
                        self.snacks.append(pos)
                        break

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
        self.spawn_snack(1)

    def print_setup(self):
        print(f'height x width: {self.dimensions[0]} x {self.dimensions[1]}')

    def print_status(self):
        self.clear_terminal()
        self.print_world()
        print(f'moves: {self.moves}')

    def finish(self):
        if self.verbose in ('minimal', 'very'):
            self.clear_terminal()
            self.print_world()
            self.print_setup()
            print(f'Moves: {self.moves}')
            print(f'Segments: {len(self.segments)}')
            print(f'reason: {self.status}')
            time.sleep(1)

    def main(self):
        self.initialize()
        while True:

            self.write_buffer()
            self.check_status()

            if self.status != 'okay':
                self.finish()
                break
            elif self.status == 'okay':
                try:
                    self.step()
                    if self.verbose == 'verbose':
                        self.print_status()
                except KeyboardInterrupt:
                    sys.exit()
            else:
                break

###############################################################################

class Snake_version_2(Snake):

    def set_directions(self):
        #tupel aus dictionary abgreifen
        directions = list(self.directions)
        random.shuffle(directions)

        snack_y = self.snacks[0][0]
        snack_x = self.snacks[0][1]
        head_y, head_x = self.head

        if random.randint(0,1):
            if head_y < 3:
                #directions.remove('S')
                directions.insert(0, 'S')
            elif head_y > self.dimensions[0] - 2:
                #directions.remove('N')
                directions.insert(0, 'N')
            else:
                pass
            if head_x < 3:
                #directions.remove('E')
                directions.insert(0, 'E')
            elif head_y > self.dimensions[0] - 2:
                #directions.remove('W')
                directions.insert(0, 'W')
            else:
                pass

        if head_y == snack_y and head_x > snack_x:
            #directions.remove('W')
            directions.insert(0, 'W')
        elif head_y == snack_y and head_x < snack_x:
            #directions.remove('E')
            directions.insert(0, 'E')
        elif head_x == snack_x and head_y < snack_y:
            #directions.remove('S')
            directions.insert(0, 'S')
        else:
            #directions.remove('N')
            directions.insert(0, 'N')

        return directions

###############################################################################

class Snake_circle(Snake):

    def turn_right(self):
        headings = ['N', 'E', 'S', 'W',]
        location = headings.index(self.heading)
        if location < 3:
            self.heading = headings[location + 1]
        else:
            self.heading = 'N'

    def set_directions(self):
        snack_y, snack_x = self.snacks[0]
        directions = []
        surroundings = self.get_surroundings()
        head_y, head_x = self.head
        if self.head[0] <= snack_y and self.head[1] == snack_x:
            if self.heading in ('N'):
                directions.append('N')
            else:
                self.heading = 'S'
                directions.append('S')
        elif surroundings[self.heading] in (' ', 's'):
            directions.append(self.heading)
        else:
            self.turn_right()
        return directions
