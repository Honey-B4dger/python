import os

all_files = os.listdir()

python_files = []

for element in all_files:
    if '.py' in element:
        python_files.append(element)

lines = 0
words = 0
for file in python_files:
    with open(file) as f:
        for line in f:
            lines +=1
            words += len(line.split())

print('This project involves:')
print(f'{lines} lines of code with {words} words, ', end = '')
print(f'distributed over {len(python_files)} python-files.')
