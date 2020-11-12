base = 1
while True:
    square = base**2
    if len(str(square)) > 3:
        print((base - 1)**2)
        break
    base += 1
