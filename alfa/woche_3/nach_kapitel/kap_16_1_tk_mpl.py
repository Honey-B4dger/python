from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

fig = Figure(figsize = (9, 6), facecolor = "white") 
axis = fig.add_subplot(111)

t = list(range(0, 10, 1))                     # erzeugt Eingabeliste 
t = [float(x) for x in t]
tt = [x**2 for x in t]
ttt = [x**3 for x in t]

axis.set_xticks([0, 2.5, 5,7.5, 10])
axis.set_yticks([0, 250, 500, 750,1000])
axis.set_ylim(0, 800)
axis.set_xlabel("Quadrat- und Kubik-Kurve")
axis.xaxis.grid(True, which="minor")
axis.yaxis.tick_right()

axis.grid()

root = tk.Tk()
root.title("Quadriert vs. Kubisch")

canvas = FigureCanvasTkAgg(fig, master = root)     # matplotlib Zeichenflaeche
canvas._tkcanvas.grid(row=0,column = 1,rowspan=20) #

def plot1(): 
    axis.plot(t, tt, "-r", label = "Squared")
    canvas.draw()
def plot2(): 
    axis.plot(t, ttt, "--g", label = "Cubed")
    canvas.draw()

b1 = tk.Button(master=root, text="Plot 1", command=plot1)                # Plot 1    
b1.grid(row=0,column = 0,sticky = tk.N+tk.W+tk.S+tk.E) #
b2 = tk.Button(master=root, text="Plot 2", command=plot2)                # Plot 2   
b2.grid(row=1,column = 0,sticky = tk.N+tk.W+tk.S+tk.E) #
button = tk.Button(master=root, text="Quit", command=quit)               # Tkinter Button    
button.grid(row=2,column = 0,sticky = tk.N+tk.W+tk.S+tk.E) #

root.mainloop()
