with open('textfile.txt', 'r') as f:
    content = f.read()

print(type(content))
print(content.strip())

with open('cat.png', 'rb') as f:
    cat_content = []
    for line in f:
        cat_content.append(line)

print(len(cat_content))
print(len(cat_content[0]))

for line in cat_content:
    print(line)
