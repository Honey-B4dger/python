results = []
def get_digit(number, nth):
    length = len(str(number))
    return (number // 10 **(length - nth)) % 10

for a in range(10):
    for b in range(10):
        for c in range(10):
            if (a + b + c) % 2 == 1:
                results.append(int(str(a) + str(b) + str(c)))

print(len(results))
