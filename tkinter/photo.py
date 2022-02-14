from tkinter import *
from PIL import Image, ImageTk

root=Tk()

root.geometry("487x390")
# jpg is not supported here
# photo=PhotoImage(file="11.png")


# for jpg install pillow library and follow this code
img=Image.open("./tkinter/img1.jpg")


photo=ImageTk.PhotoImage(img)
label=Label(image=photo)
label.pack()

root.mainloop()