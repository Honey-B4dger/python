import os
import random

with open('hangman_ASCII_inverted.txt', 'r') as file:
    hangman_graphics = file.readlines()

class Hangman():
    def __init__(self):
        #self.wort = [char.upper() for char in wort]
        self.loesung = []
        self.zulaessige_versuche = 6
        self.geratene_chars = []
        self.geloest = False
        self.fail = False
        self.fails = 0

    def gen_word(self):
        with open('woerter.txt', 'r') as f:
            woerter = f.read().split()
        self.wort = random.choice(woerter)
        self.wort = self.wort.upper()


    def gen_hangman(self):
        start = self.fails
        return ''.join(hangman_graphics[start * 7 : start * 7 + 7])


    def sgl_char(self, c):
        if c.isalpha() and len(c) == 1:
            return True
        else:
            return False

    def gen_result(self):
        self.loesung = []
        for char in self.wort:
            if char in self.geratene_chars:
                self.loesung.append(char)
            else:
                self.loesung.append('_')
        return self.loesung

    def try_char(self, char):
        char = char.upper()
        if self.sgl_char(char) and char.isalpha() and char not in self.geratene_chars:
            self.geratene_chars.append(char)
            if char in self.wort:
                print(f"Gute Wahl! {char} kommt in dem Wort vor.")
#        else:
#            input('Bitte einen anderen Buchstaben probieren: ')
        if char not in self.wort:
            self.fails += 1
            print(f"{char} kommt leider nicht in dem Wort vor.")


    def check_complete(self):
        if self.wort == ''.join(self.loesung):
            self.geloest = True
        if self.fails >= self.zulaessige_versuche:
           self.fail = True 
