import maze

m = maze.Maze('maze_map.txt')

m.initialize()
m.print_map()
m.seen[1][1] = 'O'
m.seen[3][1] = 'O'
m.cursor = (1,8)
m.print_map()

for key in m.directions.items():
    print(key)
