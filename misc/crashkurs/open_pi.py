with open('pi.txt') as f:
    content = f.readlines()

print(content)

strng = str()
for line in content:
    strng += line.strip()

print(strng)
print(len(strng))
