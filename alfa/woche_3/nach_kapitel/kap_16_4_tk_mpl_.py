from tkinter import *
from tkinter import filedialog,simpledialog
import json
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt 

class Plotwindow():    
    def __init__(self, masterframe, size):        
        (w,h)=size            
        self.figure = plt.Figure(size)        
        self.axes = self.figure.add_subplot(111)        
        # create canvas as matplotlib drawing area        
        res = self.canvas = FigureCanvasTkAgg(self.figure, master=masterframe)        
        self.canvas.get_tk_widget().grid()    # Get reference to tk_widget
        print(res)
#        print (self.canvas.get_tk_widget())
    def plotxy(self, x, y):        
        self.axes.scatter(x,y)      
        self.canvas.draw()       
    def clearplot(self):
        self.axes.cla()              # clear axes
        self.canvas.draw() 

class ReadData():

    def __init__(self):
        self.index=0        # index of function call

    def myscat(self):
        filename = 'data/eq_data_1_day_m1.json' # anpassen an lokalen Pfad erforderlich
        with open(filename) as f:
            all_eq_data = json.load(f)
        all_eq_dicts = all_eq_data['features']
        mags, plas, lons, lats = [], [], [], []
        for eq_dict in all_eq_dicts:
            mag = eq_dict['properties']['mag']
            pla = eq_dict['properties']['place']
            lon = eq_dict['geometry']['coordinates'][0]
            lat = eq_dict['geometry']['coordinates'][1]
            mags.append(mag)
            plas.append(pla)
            lons.append(lon)
            lats.append(lat)
        return mags,lats

def plotdata():
    b2.invoke()
    x,y = datrd.myscat()
    plot_w.plotxy(x,y)

def clear():    
    plot_w.clearplot()

if __name__ == "__main__":  # verhindert Start bei Import; ermöglicht Start bei Ausführung als Executable. 
    
    datrd = ReadData()
    root = Tk()
    root.title("MyPlot")
    mainframe = Frame(root)
    plot_w = Plotwindow(mainframe,(8,6))
    mainframe.grid(row = 0,rowspan = 8,column = 1)
    buttonframe = Frame(root)
    buttonframe.grid(row=0,column=0,padx=10 )    
    b1 = Button(buttonframe,text="Plot", command = plotdata, activeforeground="red") #
    b1.grid(row=0,column=0,sticky=N+S+E+W,padx=10)    
    b2 = Button(buttonframe,text="Clear", command = clear)
    b2.config(activeforeground = "red")    
    b2.grid(row=1,column=0,sticky=N+S+E+W,padx=10)    
    b3 = Button(buttonframe,text="Close", command = root.destroy, activeforeground="red")    
    b3.grid(row=2,column=0,sticky=N+S+E+W,padx=10)    
    root.mainloop()
