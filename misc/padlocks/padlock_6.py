possibilities = []
valids = []

for a in range(10):
    for b in range(10):
        for c in range(10):
            possibilities.append([a, b, c])

for possibility in possibilities:
    for digit in range(3):
        pos = possibility.copy()
        reference = pos[digit]
        pos.pop(digit)
        if reference == sum(pos):
            valids.append(possibility)
            print(possibility, digit, sum(pos))

print(len(valids))

