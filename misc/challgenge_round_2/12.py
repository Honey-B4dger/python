with open('resources/evil2.gfx', 'rb') as file:
    raw = file.read()

#print(raw)
print(len(raw))

print(raw[1])

r_1 = open('resources/evil2_1.jpg', 'ab')
r_2 = open('resources/evil2_2.jpg', 'ab')
r_3 = open('resources/evil2_3.jpg', 'ab')
r_4 = open('resources/evil2_4.jpg', 'ab')
r_5 = open('resources/evil2_5.jpg', 'ab')

for i in range(len(raw)):
    if i % 5 == 0:
        r_1.write(raw[i])
