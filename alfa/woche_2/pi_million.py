with open('pi_million_digits.txt') as f:
    pi_strng = ''
    for line in f:
        #print(line.strip())
        pi_strng += line.strip()

print(pi_strng)

print('130585' in pi_strng)
