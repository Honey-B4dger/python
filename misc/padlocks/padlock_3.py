results = []
def get_digit(number, nth):
    length = len(str(number))
    return (number // 10 **(length - nth)) % 10

for a in range(10):
    for b in range(10):
        for c in range(10):
            if a%2 == 0 and b%2 == 0 and c%2 == 0:
                results.append(int(str(a) + str(b) + str(c)))

print(len(results))
"""
print(get_digit(123,1))
print(get_digit(123,2))
print(get_digit(123,3))
"""
