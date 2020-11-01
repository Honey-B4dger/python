with open('hangman_ASCII.py', 'r') as file:
    hangman_graphics = file.readlines()

#print('\n'.join(hangman_graphics[1:7]))

#print(len(hangman_graphics))

"""
for i in range(1, 50, 7):
    print('\n'.join(hangman_graphics[i: i + 7]))
"""

# 1, 8, 15

def print_hangman(errors):
    start = 1 + errors * 7
    return '\n'.join(hangman_graphics[start : start + 7])


for i in range(7):
    print(print_hangman(i))


