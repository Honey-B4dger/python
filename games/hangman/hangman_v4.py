import os
import random
import hangman

version = 'HANGMAN Version 1.0'
clear = lambda: os.system('clear')
conti = lambda: input('Zum Fortfahren die Eingabetaste drücken...')

clear()
h = hangman.Hangman()
h.gen_word()

print(version)
print('')
print('Hallo Maus, ich möchte eine Runde Hangman mit dir spielen')
print(f'Das Wort hat {len(h.wort)} Buchstaben und du hast 7 Versuche.')
print('')
print('Viel Glück!')
print('')
conti()

while True:
    clear()
    print(h.gen_hangman())
    print(f"Lösung: {' '.join(h.gen_result())}")


    if len(h.geratene_chars) == 0:
        print('Bisher hast du noch keine Buchstaben geraten\n')
    else:
        print(f"Bisher geratene Buchstaben: \n {' '.join(h.geratene_chars)}\n")

    char = input('Bitte rate einen Buchstaben: ')
    h.try_char(char)
    print('')
    h.gen_result()
    h.check_complete()

    if h.geloest or h.fail:
        break
    else:
        conti()

clear()
if h.geloest == True:
    print(h.gen_hangman())
    print(f"Gratulation! Du hast das Wort erraten: {' '.join(h.wort)}")
elif h.fail == True:
    print(h.gen_hangman())
    print(f"Schade. Du hast das Wort nicht erraten: {' '.join(h.wort)}")

print('')
