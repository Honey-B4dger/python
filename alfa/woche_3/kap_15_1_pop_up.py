from tkinter import *
from tkinter import filedialog

def callback():
    root = Tk()
#    root.update()
    filetypes = [("json files","*.json"),("All files","*.*")]
    initialdir="C:/users/alfa/python"
    fname = ''
    filedialog.askopenfilename(filetypes=filetypes,initialdir=initialdir,title="Select File:")
    print (fname,type(fname))
    root.destroy()
    return fname

b = Button(text = 'Open File', command = callback, height = 2, width = 10).pack(fill=X)
c = Button(text = 'Quit', command=quit,height=2,width=10).pack(fill=X)

mainloop()
