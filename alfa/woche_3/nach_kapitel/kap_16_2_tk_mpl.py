import tkinter # Example with key binding; press key
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

root = tkinter.Tk()
root.wm_title("Einbetten von matplotlib in tkinter")

fig = Figure(figsize=(5, 4), dpi=100)         # erzeugt matplotlib.figure objekt
t = list(range(0, 30, 1))                     # erzeugt Eingabeliste 
t = [float(x) for x in t]
tt = [x**2 for x in t]
fig1 = fig.add_subplot(111)                   # erzeugt axes subplot objekt
#print(fig1)
fig1.plot(t, tt)                              # matplotlib plot Funktion

canvas = FigureCanvasTkAgg(fig, master=root)  # Eine tk Zeichenfläche für matplotlib plots
canvas.draw()                                 # Bildaufbau
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root) # matplotlib navigation toolbar
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):                                # matplotlib key event handler
    print("Taste {} wurde gedrückt.".format(event.key))
    print(event.x, event.y)
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect("key_press_event", on_key_press)     # Verbindung des Event handlers mit Callback-Funktion

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

text = tkinter.Label(root,text="Drücken Sie Tasten, z.B. p oder s")
text.pack()

button = tkinter.Button(master=root, text="Quit", command=_quit)                # Tkinter Button    
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
# Wird root.destroy() verwendet, erfolgt eine Fehlermeldung im Fall des Schliessens das Fensters 
# mit dem Window manager.
