import random

usr_num = input('Bitte gib eine Zahl ein: ')
print('')

roll = [random.randint(1,6) for i in range(3)]

#print(roll)

sum = 0
for num in roll:
    sum += num

#print(sum)

print(f'Du hast die Zahl {usr_num} angegeben.')
print('')
print(f'Die gewürfelten Augen sind {roll[0]}, {roll[1]}, {roll[2]}')
