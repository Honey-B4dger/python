class hangman():
    def __init__(self,wort):
        self.wort = wort.upper()
        self.laenge = len(self.wort)
        self.anzahlVersuche = 0
        self.gerateneBuchstaben = set()
        self.loesung = [' ' for i in range(self.laenge)]
        self.erlaubteVersuche = 5
        self.geloest = False

    def korrekter_buchstabe(self,char):
        for i in range(self.laenge):
            if self.wort[i] == char:
                self.loesung[i] = char
                return(self.loesung)
        if self.wort == self.loesung:
            self.geloest = True

    def verbleibende_versuche(self):
        self.anzahlVersuche += 1
        if self.anzahlVersuche > self.erlaubteVersuche:
            return False
        else:
            return True

h = hangman ('test')

print(h.wort)
print(h.anzahlVersuche)
print(h.gerateneBuchstaben)
print(h.loesung)

while h.geloest == False:
    print(h.geloest)
    guess = (input('Bitte einen Buchstaben raten: ')).upper()
    if len(guess) == 1 and guess.isalpha():
        if guess not in h.gerateneBuchstaben and guess in h.wort:
            print(h.korrekter_buchstabe(guess))
    if h.geloest == True:
        break


