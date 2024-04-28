import tkinter as tk
from tkinter import Toplevel
from tkinter import *
Projects=['Placeholder','Test']

def open_project():
    opening_window=tk.Toplevel()
    opening_window.title('Opening')
    opening_window.geometry('400x400')
    openlabel=tk.Label(opening_window,text="Which would you like to open?(by#)").grid(row=0,column=0)
    tk.Label(opening_window,font=('Arial','18'),text=Projects).grid(row=(1),column=0)
    enteropen=tk.Entry(opening_window)
    enteropen.grid(row=2,column=0)
    
    def confirm_open():
        var1=(int(enteropen.get()))-1
        var2=Projects
        
        opendetails=open("Desktop/ForBino/Projects/"+(var2[var1]+'.txt'),'r')
        stuff = opendetails.read()
        rootText.insert(END, stuff)
        opening_window.destroy()
        
    tk.Button(opening_window,text="Open",command=confirm_open).grid(row=2,column=1)
def add_project():
    True

root=tk.Tk()
root.title("Test")
root.geometry("400x400")

rootLabel=tk.Label(root,text="Would you like to Open a project or Add one?",font=("Arial","10")).grid(row=0,column=0)

rootText=tk.Text(root,height='5',width='20')
rootText.grid(row=2,column=0)

rootOpen=tk.Button(root,width=3,height=2,text="Open",command=open_project).grid(row=1,column=0)

rootAdd=tk.Button(root,width=3,height=2,text="Add",command=add_project).grid(row=1,column=1)

root.mainloop()