import os

os.system('clear')

chars = [chr(i) for i in range(65, 75)]
nums = list(range(1, 11))

#print(chars)
#print(nums)

table = []

table.append(chars)

for num in nums:
    temp = []
    for char in chars:
        temp.append(f'{char}{num}')
    table.append(temp)

for row in table:
    print('\t'.join(row))

################################################################################
# Zeilen zu Spalte

table_tp = []
for i in range(len(chars)):
    table_tp.append([])

for row in table:
    for column, item in enumerate(row):
        table_tp[column].append(item)

print('')
# drucken
for row in table_tp:
    print('\t'.join(row))

