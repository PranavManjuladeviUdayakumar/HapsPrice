import tkinter
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import ctypes
import os

 
ctypes.windll.shcore.SetProcessDpiAwareness(1)
GUI = tkinter.Tk()
GUI.geometry('1920x1080')
def func():  # function of the button
    tkinter.messagebox.showinfo("A dialog box", "Hello World")

# Create a photoimage object of the image in the path
road1=Image.open("road1.png")
road=road1.resize((100,100))
road_1=ImageTk.PhotoImage(road)
roadlabel=Label(GUI, image=road_1)
roadlabel.place(x=0, y=0)
GUI.mainloop()




#btn=tkinter.Button(GUI,text="Click Me", width=10,height=5,command=func)
#btn.place(x=0,y=0)
#GUI.mainloop()