def step():
    if ziffer[cursor] < 9:
        ziffer += 1
        if loesung_moeglich():
            cursor += 1
    else:
        backtrack()

def backtrack():
    ziffer[cursor] = 0
    cursor -= 1

while check_solution() == False:
    try:
        step()
    except IndexError:
        break
