strng = "Hello World"
res = ''

for i, char in enumerate(strng):
    if i % 2 ==  0:
        res += char.upper()
    else:
        res += char.lower()

print(res)

