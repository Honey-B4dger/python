import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askyesno
import json
from eq_plotter import eqPlotter

class FileOpener():
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.filename = ''
        self.data = []

    def ask_for_file(self):
        filetypes = [('json', '*.json')]
        self.filename = askopenfilename(filetypes=filetypes)

    def get_filename(self):
        if self.filename:
            return self.filename
        else:
            pass

if __name__ == '__main__':

    while True:
        fo = FileOpener()
        fo.ask_for_file()

        eq = eqPlotter(fo.get_filename())
        eq.open_file()
        eq.print_readable()
        eq.plot_data()

        #continue_ = askyesno('Sollen weitere Daten verarbeitet werden?')

        if askyesno('Sollen weitere Daten verarbeitet werden?'):
            continue
        else:
            break
