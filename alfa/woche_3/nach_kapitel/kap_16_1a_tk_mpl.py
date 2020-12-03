from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
#import matplotlib
#matplotlib.use("TkAgg")

import tkinter as tk

fig = Figure(figsize = (9, 6), facecolor = "white")
#axis2 = fig.add_subplot(211)
#axis = fig.add_subplot(212)
axis = fig.add_subplot(111)

t = list(range(0, 10, 1))                     # erzeugt Eingabeliste 
t = [float(x) for x in t]
tt = [x**2 for x in t]
ttt = [x**3 for x in t]


axis.set_xticks([0, 1, 5,10])
axis.set_yticks([0, 100, 500, 1000])
axis.set_ylim(0, 800)
axis.set_xlabel("Quadrat- und Kubik-Kurve")


axis.grid() # Dies ist KEIN geometriemanager, sondern ein Gitternetz in der Zeichenfläche!!!

root = tk.Tk()                                         # Tkinter wird initialisiert
root.title("Quadriert vs. Kubisch")

canvas = FigureCanvasTkAgg(fig, master = root)
#canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = 1) #
canvas._tkcanvas.pack()

toolbar = NavigationToolbar2Tk(canvas, root) # matplotlib navigation toolbar
toolbar.update()
canvas.get_tk_widget().pack()


def plot1(): 
    axis.plot(t, tt, "-r", label = "Squared")
#    print("plot1")
    canvas.draw()
#    axis.legend()
def plot2(): 
    axis.plot(t, ttt, "--g", label = "Cubed")
    canvas.draw()
#    axis.legend()

b1 = tk.Button(root, text="Plot 1", command=plot1)                # Tkinter Button    
b1.pack() #
b2 = tk.Button(root, text="Plot 2", command=plot2)                # Tkinter Button    
b2.pack()
button = tk.Button(root, text="Quit", command=quit)                # Tkinter Button    
button.pack()

root.mainloop()
