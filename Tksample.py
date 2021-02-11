from tkinter import *
from tkinter import ttk

root = Tk()
root.minsize(width=250, height=150)

frame = ttk.Frame(root, padding=10)
frame2 = ttk.Frame(
    frame, width=200, height=100,
    borderwidth=10, relief='sunken')

frame.pack()
frame2.pack()
root.mainloop()
