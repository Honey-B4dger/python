from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.geometry=("900x900")

textVar = StringVar()
listVar = StringVar() # .get()/.set()

optionList = ["option1", "option2", "option3"]
omVar = StringVar()

textVar.set("I am an Entry Widget")
listVar.set("Item1 Item2 Item3 Item4 Item5 Item6 Item7 Item8 Item9 Item10 Item11 Item12")
omVar.set("option1")

f = Frame(root)
f.grid(sticky="nsew")

l1 = Label(f,text="Some Tkinter Widgets ",font=("times","20")) # Label or Entry widgets: 
l1.grid(row=0,column=0,columnspan=2,sticky="nsew")                         # assign values with (tkinterVar).set/.get(newVal)   

#l2 = Label(f,text="I am a Label Widget",fg="blue") # 
l2 = Label(f,text="I am a Label Widget",fg="blue",font=("default",12)) # 
l2.grid(row=2,column=0,sticky=E+W)       

stvar="disabled"
stvar="normal" # 
#stvar="active"

e1 = Entry(f,textvariable = textVar, state = stvar,font=("default",12), relief="groove")     #  
e1.grid(row=2,column=1)

lf = LabelFrame(f,text="I am a LabelFrame")
lf.grid(row=3, column=0, columnspan=2,sticky=N+S+E+W)

lb = Listbox(lf,listvariable=listVar)
lb.grid(row=4,column=0,columnspan=2,sticky=N+S+E+W)

l4 = Label(lf,text="I am an OptionMenu") # When Label or Entry widgets
l4.grid(row=5,column=0,sticky=E+W)       

om = ttk.OptionMenu(lf,omVar, "option1",optionList)
om.grid(row=5, column=1)

l4 = Label(lf,text="I am a Spinbox") # When Label or Entry widgets
l4.grid(row=6,column=0,sticky=E+W)       

spinbox = Spinbox(lf, from_=1, to=10,bd=1) # borderwidth ist die Breite des Randes
spinbox.grid(row=6,column = 1)

nb = ttk.Notebook(lf)
tab1 = ttk.Frame(nb)
tab2 = ttk.Frame(nb)
nb.add(tab1, text="Tab 1")
nb.add(tab2, text="Tab 2")
nb.grid()
ttk.Label(tab1,text="Hi there, \nI am a notebook Label, \n located at tab 1").grid()
ttk.Label(tab2,text="Hi there, \nI am also a notebook Label, \nbut I\'m located at tab 2").grid()

b1 = Button(root,text="Press Me to Quit",command=root.quit)
b1.grid(row=7,column=0, columnspan =2,sticky=E+W)

root.title('Sample application')
root.mainloop() 
