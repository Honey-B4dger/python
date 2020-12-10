import tkinter as tk
from tkinter.filedialog import askopenfile
from tkinter.filedialog import askopenfile

root = tk.Tk()

title = tk.Label(root, text="Sudoku Grid Creator")
title.pack()

root.mainloop()


if __name__ == '__main__':
    filename = askopenfile()
