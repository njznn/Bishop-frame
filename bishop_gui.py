import tkinter as tk
import matplotlib
import numexpr as ne
import sys
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg as tkagg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
from binding import *
from mpl_toolkits.mplot3d import Axes3D
import ast
matplotlib.use("Agg")

UNARY_OPS = (ast.UAdd, ast.USub)
BINARY_OPS = (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod)

class App:
    def __init__(self, master):
        self.master = master

        #needed variables
        self.x = 0
        self.y = 0
        self.z = 0
        self.tangents = 0
        self.normals = 0
        self.binormals = 0
        self.Npoints = 0
        self.Nscalpts = 1
        self.MAINCORDS = 0
        self.slider1 = 0
        self.slider2 = 0
        self.slider3 = 0
        self.slider = 0

        #plot config
        self.figure = Figure(figsize=(5, 4))
        self.ax = self.figure.add_subplot(projection='3d')
        self.canvas = FigureCanvasTkAgg(self.figure, master=master)
        self.canvas.get_tk_widget().grid(row=18, column=0, columnspan=2)
        self.camerasettings = [self.ax.azim, self.ax.elev, self.ax.get_proj()[:3, 3]]
        self.zoomsettings = []


        #frontend:
        self.draw_buttonleft = tk.Button(master, text="Draw" ,command=self.drawleft)
        self.draw_buttonright = tk.Button(master, text="Draw" ,command=self.drawright)
        self.draw_buttondown = tk.Button(master, text="Download" ,command=self.download)


        self.text_file_entry = tk.Entry(master)
        self.text_initvec_entry = tk.Entry(master)
        self.text_initvec_entryr = tk.Entry(master)
        self.ft_entry = tk.Entry(master)
        self.text_initvec_entry = tk.Entry(master)
        self.entry_tpar = tk.Entry(master)
        self.entry_downpath = tk.Entry(master)
        
        #default:
        self.text_initvec_entryr.insert(0,"0,1,0")
        self.ft_entry.insert(0,"t,0,0")
        self.entry_tpar.insert(0,"0,10,20")

        #labels
        label0 = tk.Label(text="INSERT CURVE COORDINATES:", font=('Calibri', 12, 'bold'))
        label1 = tk.Label(text="/path_to_file/file.txt")
        label2 = tk.Label(text="required format:")
        label3 = tk.Label(text="x1  y1  z1 ")
        label4 = tk.Label(text="x2  y2  z2 ")
        label5 = tk.Label(text="x3  y3  z3 ")
        label6 = tk.Label(text=" :   :   : ")
        label7 = tk.Label(text="INSERT random vector as x,y,z")
        label7r = tk.Label(text="INSERT random vector \nas x,y,z")
        label_t = tk.Label(text="PARAMETRIC CURVE:", font=('Calibri', 12, 'bold'))
        label_tpar = tk.Label(text="INSERT t param as \ntmin,tmax,tpoints")
        label_ft = tk.Label(text="INSERT f(t) as \n fx(t),fy(t),fz(t)")
        label_ndir = tk.Label(text="draw every N base:")
        label_tsc = tk.Label(text="T scale(%):")
        label_d1sc = tk.Label(text="d1 scale(%):")
        label_d2sc = tk.Label(text="d2 scale(%):")
        label_download = tk.Label(text="Enter to download: /path/filename.txt")


        #grid positions of labels
        label0.grid(row=0, column=0)
        label1.grid(row=1, column=0)
        label2.grid(row=3, column=0)
        label_t.grid(row=0, column=1, columnspan=1,sticky="e", padx=(80,10))
        label_tpar.grid(row=1, column=1, columnspan=1, padx=(70,0), pady=(5))
        label3.grid(row=4, column=0)
        label4.grid(row=5, column=0)
        label5.grid(row=6, column=0)
        label6.grid(row=7, column=0)
        label7.grid(row=8, column=0)
        label7r.grid(row=8, column=1, padx=(70,0))
        label_ndir.grid(row=26, column=0, padx=(0,0))
        label_tsc.grid(row=26, column=1, padx=(0,0))
        label_d1sc.grid(row=28, column=0, padx=(0,150))
        label_d2sc.grid(row=28, column=1, padx=(0,150))
        label_download.grid(row=32, column=0, padx=(50,0))

        self.text_file_entry.grid(row=2, column=0)
        self.text_initvec_entry.grid(row=9, column = 0)
        self.text_initvec_entryr.grid(row=9, column = 1, padx=(55,0))
        self.draw_buttonleft.grid(row=10, column=0, sticky="e", padx=(0,100))
        self.draw_buttonright.grid(row=10, column=1, sticky="e", padx=(0,80))
        self.draw_buttondown.grid(row=33, column =1)
        self.entry_downpath.grid(row=33, column=0)
    
        label_ft.grid(row=4, column = 1, padx=(50,0))
        self.ft_entry.grid(row=5, column=1, sticky="e", padx=(0,30))
        self.entry_tpar.grid(row=2, column=1, sticky="e", padx=(0,30))


    #when user presses right draw button:
    def drawright(self):
        self.ax.clear()

        entry_tpar = self.entry_tpar.get()
        vect = entry_tpar.replace(' ', '').split(',')
        try:
            vect[0] = ne.evaluate(vect[0])
            vect[1] = ne.evaluate(vect[1])
            vect[2] = int(vect[2])
            self.Npoints = vect[2]
            self.entry_tpar.config(fg="black")
            if vect[1] < vect[0]:
                raise TypeError
            elif (len(vect)!=3):
                raise ValueError
            
        except TypeError:
            self.entry_tpar.config(fg="red")
            print('tmax must be bigger than tmin')
        except ValueError:
            self.entry_tpar.config(fg="red")
            print('Initial vector is not convertible to float')

        t = np.linspace(vect[0], vect[1], vect[2])
        #for parametric funciton expression entry
        

        text_initvec_entryr = self.text_initvec_entryr.get()
        vec = text_initvec_entryr.strip().split(',')
        try:
            vec[0] = float(vec[0])
            vec[1] = float(vec[1])
            vec[2] = float(vec[2])
            self.text_initvec_entryr.config(fg="black")
            if (len(vec)!=3):
                raise ValueError
            
        except ValueError:
            self.text_initvec_entryr.config(fg="red")
            print('Initial vector is not convertible to float')
        
        
        ft_entry = self.ft_entry.get()
        vecf = ft_entry.replace(' ', '').split(',')
        
        try:
            self.ft_entry.config(fg="black")
            xcor = np.ones(len(t))*ne.evaluate(vecf[0]) if np.isscalar(vecf[0]) else ne.evaluate(vecf[0]) 
            ycor = np.ones(len(t))*ne.evaluate(vecf[1]) if np.isscalar(vecf[1]) else ne.evaluate(vecf[1])
            zcor = np.ones(len(t))*ne.evaluate(vecf[2]) if np.isscalar(vecf[2]) else ne.evaluate(vecf[2])
            coords = np.column_stack((xcor,ycor, zcor))
        except:
            self.ft_entry.config(fg="red")
            print('Wrong expression form')

        # calculation in c++
        maincords = calcincpp(coords, vec)
        self.MAINCORDS = maincords
        #plot
        
        x = maincords[0,::4]
        y = maincords[1,::4]
        z = maincords[2,::4]
        tangents = maincords[:, 1::4]
        normals = maincords[:, 2::4]
        binormals = maincords[:, 3::4]

        
        self.ax.plot(x,y,z, color='black')
        
        self.x, self.y, self.z, self.tangents, self.normals, self.binormals = (
        x,y,z,tangents, normals, binormals)
        

        self.ax.quiver(self.x[:-1],self.y[:-1],self.z[:-1], self.tangents[0], 
                  self.tangents[1], self.tangents[2], color='red', label='Tangent')
        self.ax.quiver(self.x[:-1],self.y[:-1],self.z[:-1], self.normals[0],
                  self.normals[1], self.normals[2], color='green', label='Normal')
        self.ax.quiver(self.x[:-1],self.y[:-1],self.z[:-1], self.binormals[0],
                  self.binormals[1], self.binormals[2], color='purple', label='Binormal')
        self.ax.set_aspect('auto')
        self.zoomsettings = [self.ax.get_xlim(), self.ax.get_ylim(), self.ax.get_zlim()]


        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=18, column=0, columnspan=2)
        #toolbar
        toolbarFrame = tk.Frame(master=self.master)
        toolbarFrame.grid(row=25,column=0, columnspan=2)
        toolbar = NavigationToolbar2Tk(self.canvas, toolbarFrame)

        #sliders
        self.slider = tk.Scale(master=self.master, from_ = 1, to= self.Npoints , 
                          orient=tk.HORIZONTAL, command=self.npointscommand)
        self.slider.grid(row=27, column = 0, padx=(0,0))

        self.slider1 = tk.Scale(master=self.master, from_ = 0, to= 500 , 
                          orient=tk.HORIZONTAL, command=self.scale_base_T)
        self.slider1.grid(row=27, column = 1, padx=(0,0))
        self.slider1.set(100)

        self.slider2 = tk.Scale(master=self.master, from_ = 0, to= 500 , 
                          orient=tk.HORIZONTAL, command=self.scale_base_d1)
        self.slider2.grid(row=28, column = 0, padx=(60,0))
        self.slider2.set(100)

        self.slider3 = tk.Scale(master=self.master, from_ = 0, to = 500 , 
                          orient=tk.HORIZONTAL, command=self.scale_base_d2)
        self.slider3.grid(row=28, column = 1, padx=(60,0))
        self.slider3.set(100)

    #when user presses right draw button:
    def drawleft(self):
        self.ax.clear()

        text_initvec_entry = self.text_initvec_entry.get()
        vec = text_initvec_entry.strip().split(',')
        try:
            vec[0] = float(vec[0])
            vec[1] = float(vec[1])
            vec[2] = float(vec[2])
            self.text_initvec_entry.config(fg="black")
            if (len(vec)!=3):
                raise ValueError
            
        except ValueError:
            self.text_initvec_entry.config(fg="red")
            print('Initial vector is not convertible to float')
        


        text_file_path = self.text_file_entry.get()
        try:
            coords = np.loadtxt(text_file_path, dtype=np.float64)
            self.text_file_entry.config(fg="black")
            if(not coords.shape[1]==3):
                self.text_file_entry.config(fg="red")
                print("Format is not right")
                 
        except FileNotFoundError:
             self.text_file_entry.config(fg="red")
             print("File not found")
        except NotADirectoryError:
             self.text_file_entry.config(fg="red")
             print("File not found")

        # calculation in c++
        maincords = calcincpp(coords, vec)
        self.MAINCORDS = maincords
        #plot
        
        x = maincords[0,::4]
        y = maincords[1,::4]
        z = maincords[2,::4]
        tangents = maincords[:, 1::4]
        normals = maincords[:, 2::4]
        binormals = maincords[:, 3::4]

        
        self.ax.plot(x,y,z, color='black')
        
        self.x, self.y, self.z, self.tangents, self.normals, self.binormals = (
        x,y,z,tangents, normals, binormals)
        

        self.ax.quiver(self.x[:-1],self.y[:-1],self.z[:-1], self.tangents[0], 
                  self.tangents[1], self.tangents[2], color='red', label='Tangent')
        self.ax.quiver(self.x[:-1],self.y[:-1],self.z[:-1], self.normals[0],
                  self.normals[1], self.normals[2], color='green', label='Normal')
        self.ax.quiver(self.x[:-1],self.y[:-1],self.z[:-1], self.binormals[0],
                  self.binormals[1], self.binormals[2], color='purple', label='Binormal')
        self.ax.set_aspect('auto')
        self.zoomsettings = [self.ax.get_xlim(), self.ax.get_ylim(), self.ax.get_zlim()]


        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=18, column=0, columnspan=2)
        #toolbar
        toolbarFrame = tk.Frame(master=self.master)
        toolbarFrame.grid(row=25,column=0, columnspan=2)
        toolbar = NavigationToolbar2Tk(self.canvas, toolbarFrame)

        #sliders
        self.slider = tk.Scale(master=self.master, from_ = 1, to= self.Npoints , 
                          orient=tk.HORIZONTAL, command=self.npointscommand)
        self.slider.grid(row=27, column = 0, padx=(0,0))

        self.slider1 = tk.Scale(master=self.master, from_ = 0, to= 500 , 
                          orient=tk.HORIZONTAL, command=self.scale_base_T)
        self.slider1.grid(row=27, column = 1, padx=(0,0))
        self.slider1.set(100)

        self.slider2 = tk.Scale(master=self.master, from_ = 0, to= 500 , 
                          orient=tk.HORIZONTAL, command=self.scale_base_d1)
        self.slider2.grid(row=28, column = 0, padx=(60,0))
        self.slider2.set(100)

        self.slider3 = tk.Scale(master=self.master, from_ = 0, to = 500 , 
                          orient=tk.HORIZONTAL, command=self.scale_base_d2)
        self.slider3.grid(row=28, column = 1, padx=(60,0))
        self.slider3.set(100)


    #slider for number of base triads
    def npointscommand(self, points):
        points = int(points)
        self.Nscalpts = points
        
        self.x = self.MAINCORDS[0,::4]
        self.x=self.x[::points]
        self.y = self.MAINCORDS[1,::4]
        self.y=self.y[::points]
        self.z = self.MAINCORDS[2,::4]
        self.z=self.z[::points]
        

        vect = self.MAINCORDS[:,1::4]
        vect = vect[:,::points]
        self.tangents = vect *int(self.slider1.get())/100.0

        vectn = self.MAINCORDS[:,2::4]
        vectn = vectn[:,::points]
        self.normals = vectn * int(self.slider2.get())/100.0

        vectb = self.MAINCORDS[:,3::4]
        vectb = vectb[:,::points]
        self.binormals = vectb * int(self.slider3.get())/100.0
        #need to destroy
        if self.canvas:
            self.camerasettings = [self.ax.azim, self.ax.elev, self.ax.get_proj()[:3, 3]]
            self.zoomsettings = [self.ax.get_xlim(), self.ax.get_ylim(), self.ax.get_zlim()]
            self.ax.clear()
        self.drawagain(points)
    
    #scale tangent vector
    def scale_base_T(self, points):
        vec = self.MAINCORDS[:,1::4]
        vec = vec[:, ::self.Nscalpts]
        self.tangents = vec *int(points)/100.0

        if self.canvas:
            self.camerasettings = [self.ax.azim, self.ax.elev, self.ax.get_proj()[:3, 3]]
            self.zoomsettings = [self.ax.get_xlim(), self.ax.get_ylim(), self.ax.get_zlim()]
            self.ax.clear()
        self.drawagain(points)

    #scale director d1
    def scale_base_d1(self, points):
        d1temp = self.MAINCORDS[:,2::4]
        d1temp = d1temp[:,::self.Nscalpts]
        self.normals = d1temp* int(points)/100.0

        if self.canvas:
            self.camerasettings = [self.ax.azim, self.ax.elev, self.ax.get_proj()[:3, 3]]
            self.zoomsettings = [self.ax.get_xlim(), self.ax.get_ylim(), self.ax.get_zlim()]
            self.ax.clear()
        self.drawagain(points)
    
    #scale director d2
    def scale_base_d2(self, points):
        d2temp = self.MAINCORDS[:,3::4]
        d2temp = d2temp[:,::self.Nscalpts]
        self.binormals = d2temp* int(points)/100.0
    
        if self.canvas:
            self.camerasettings = [self.ax.azim, self.ax.elev, self.ax.get_proj()[:3, 3]]
            self.zoomsettings = [self.ax.get_xlim(), self.ax.get_ylim(), self.ax.get_zlim()]
            self.ax.clear()
        self.drawagain(points)

    #after one of the sliders change, drawagain fucntion is called
    def drawagain(self, Npoints):
        
        x = self.MAINCORDS[0,::4]
        y = self.MAINCORDS[1,::4]
        z = self.MAINCORDS[2,::4]

        self.ax.plot(x,y,z, color='black')
        
        if (len(self.x)==len(self.tangents[0])):
            self.ax.quiver(self.x,self.y,self.z, self.tangents[0], 
                    self.tangents[1], self.tangents[2], color='red', label='Tangent')
            self.ax.quiver(self.x,self.y,self.z, self.normals[0],
                    self.normals[1], self.normals[2], color='green', label='Normal')
            self.ax.quiver(self.x,self.y,self.z, self.binormals[0],
                    self.binormals[1], self.binormals[2], color='purple', label='Binormal')
            self.ax.set_aspect('auto')
        
        else:
            self.ax.quiver(self.x[:-1],self.y[:-1],self.z[:-1], self.tangents[0], 
                    self.tangents[1], self.tangents[2], color='red', label='Tangent')
            self.ax.quiver(self.x[:-1],self.y[:-1],self.z[:-1], self.normals[0],
                    self.normals[1], self.normals[2], color='green', label='Normal')
            self.ax.quiver(self.x[:-1],self.y[:-1],self.z[:-1], self.binormals[0],
                    self.binormals[1], self.binormals[2], color='purple', label='Binormal')
            self.ax.set_aspect('auto')

        self.ax.view_init(azim=self.camerasettings[0], elev=self.camerasettings[1])
        self.ax.get_proj()[:3, 3] = self.camerasettings[2]
        self.ax.set_xlim(self.zoomsettings[0])
        self.ax.set_ylim(self.zoomsettings[1])
        self.ax.set_zlim(self.zoomsettings[2])
        self.canvas.draw()
        
    #download button
    def download(self):
            text_file_path = str(self.entry_downpath.get())
            
            try:
                self.entry_downpath.config({"background": "white"})
                with open(text_file_path, "w") as f:
                    f.write("1row: x1,y2,z3, 2row: T1x T1y T1z, 3row: d1x d1y d1z, 4row: d2x d2y d2z, 5row: x2 y2 z2... \n")
                    for row in np.transpose(self.MAINCORDS):
                        f.write(" ".join(map(str, row)) + "\n")
                    print("File downloaded:", text_file_path)

            except (FileNotFoundError, UnboundLocalError):
                self.entry_downpath.config({"background": "red"})
                print("File not found")
            

        

def on_closing():
    root.destroy()

#check if number is prime, solution when slicing base vectors
def isprime(num):
    if num==2 or num==3:
        return True
    if num%2==0 or num<2:
        return False
    for n in range(3,int(num**0.5)+1,2):   
        if num%n==0:
            return False   
    return True


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


