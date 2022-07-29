import tkinter
from tkinter import messagebox
import ctypes

 
ctypes.windll.shcore.SetProcessDpiAwareness(1)
GUI = tkinter.Tk()
GUI.geometry('1920x1080')


def func():  # function of the button
    tkinter.messagebox.showinfo("A dialog box", "Hello World")

btn=tkinter.Button(GUI,text="Click Me", width=10,height=5,command=func)
btn.place(x=200,y=30)
GUI.mainloop()