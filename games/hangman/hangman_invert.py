with open('hangman_ASCII.txt', 'r') as file:
    hangman_graphics = file.read().splitlines()

inverted = open('hangman_ASCII_inverted.txt', 'a')

for line in hangman_graphics:
    if len(line) == 7:
        line += '  '
    new_line = line[::-1]
    inverted.write(new_line + '\n')
