import tkinter as tk
from tkinter.filedialog import askopenfilename
import json

class FileOpener():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry=('800x800') # funktioniert nicht
        self.filename = ''
        self.data = []

        #oberste Zeile
        self.label = tk.Label(self.root, text='Please open a file')
        self.label.grid(row=0, column=0, columnspan=2)

        #Button 'open'
        self.b = tk.Button(self.root, text='Open', command=self.callback)
        self.b.grid(row=1, column=0, columnspan=2)


        #Labels fuer die Statuszeile
        self.status_label = tk.Label(self.root, text='Status: ')
        self.status_label.grid(row=2, column=0)
        self.status_text = tk.StringVar()
        self.status_text.set('no file loaded')
        self.status = tk.Label(self.root, textvariable=self.status_text,
                               padx=5, pady=5)
        self.status.grid(row=2, column=1)

        self.root.mainloop()

    def callback(self):
        filetypes = [('json', '*.json'),('All Files', '*.*')]
        self.filename = askopenfilename(filetypes=filetypes)

        if self.filename:
            try:
                with open(self.filename) as f:
                    self.data = json.load(f)
            except:
                self.status_text.set('error')
            else:
                self.status_text.set('file loaded :)')
                print(self.data)

if __name__ == '__main__':
    fo = FileOpener()
