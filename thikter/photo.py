from cProfile import label
from tkinter import *

root=Tk()

root.geometry("487x390")

photo=PhotoImage(file="11.png")
label=Label(image=photo)
label.pack()

root.mainloop()