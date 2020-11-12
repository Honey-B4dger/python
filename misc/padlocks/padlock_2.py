possibilities = []

for a in range(10):
    for b in range(10):
        for c in range(10):
            possibilities.append(str(a) + str(b) +str(c))


print(possibilities)

valids = []

sum_ = 0

for possibility in possibilities:
    a = int(possibility[0]) 
    b = int(possibility[1]) 
    c = int(possibility[2]) 


    if a < b and b < c:
        valids.append(possibility)
        print(a, b, c)

print(len(valids))
