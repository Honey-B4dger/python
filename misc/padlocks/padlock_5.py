possibilities = []
valids = []

for a in range(10):
    for b in range(10):
        for c in range(10):
            temp = [a, b, c]
            possibilities.append(temp)

#print(possibilities)

for combination in possibilities:
    for digit in range(10):
        if combination.count(digit) >= 2:
            valids.append(combination)

print(len(valids))
