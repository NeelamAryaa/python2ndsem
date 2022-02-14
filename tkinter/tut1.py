from tkinter import *

root=Tk()

# widthxheight
root.geometry("400x300")

# width,height
root.minsize(400,300)

root.maxsize(600,400)

myLabel = Label(text="My First Tkinter GUI")
myLabel.pack()

root.mainloop()