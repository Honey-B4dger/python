from tkinter import * 
from tkinter.filedialog import askopenfilename            # Dateidialog

root = Tk()                                               # Tk() instantiieren

def callback(): 
    name = askopenfilename(filetypes = [("json","*.json"),("All Files","*.*")] ) # filetypes enthält Filter für Dateitypen
#    name = askopenfilename(filetypes = [("PNG","*.png"),("All Files","*.*")] ) # filetypes enthält Filter für Dateitypen
    print (name) 
    # Hier Lösung 14a (bestehend aus 13a) IN die Funktion schreiben



b = Button(root, text = 'Open File', command = callback)  # command = enthält den auszuführenden Befehl
b.pack(fill = X)                                          # Geometriemanager starten

root.mainloop()                                           # Eventloop starten 
