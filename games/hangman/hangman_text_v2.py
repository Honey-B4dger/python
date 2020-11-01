class Hangman():
    def __init__(self, wort):
        self.wort = wort.upper()
        self.laenge = len(wort)
        self.anzahl_versuche = 0
        self.geratene_buchstaben = []
        self.loesung = ['_', ' '] * self.laenge
        self.geloest = False

    def print_loesung(self):
        s = ''
        for char in self.loesung:
            s += char
        return s

def isSingleChar(s):
    if len(s) == 1 and s.isalpha():
        return True
    else:
        return False

def geratene_buchstaben():
    s = set()
    for element in h.geratene_buchstaben:
        s.add(element)
    print('Bisher geratene Buchstaben:')
    print(s)


h = Hangman('test')

print(h.wort)
print(h.anzahl_versuche)
print(h.geratene_buchstaben)
print(h.loesung)
print(h.print_loesung())

while h.geloest == False:

    eingabe = input('Bitte einen Buchstaben raten: ')
    eingabe = eingabe.upper()

    if isSingleChar(eingabe) and eingabe not in h.geratene_buchstaben:
        h.geratene_buchstaben.append(eingabe)
        if eingabe in h.wort:
            print('Buchstabe vorhanden')
            geratene_buchstaben()
