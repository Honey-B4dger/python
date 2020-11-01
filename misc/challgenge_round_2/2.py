with open('2_source.txt', 'r') as f:
    raw = f.read().replace('\n', '')

#print(raw)

result = [symbol for symbol in raw if symbol.isalpha()]

print(' '.join(result))
