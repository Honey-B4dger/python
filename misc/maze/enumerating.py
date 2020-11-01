with open('maze_map.txt', 'r') as f:
    content = f.read().splitlines()

print(content)
map_maze = []

for i, line in enumerate(content):
    tmp = []
    for char in line:
        tmp.append(char)
    map_maze.append(tmp)

for line in map_maze:
    print(''.join(line))
