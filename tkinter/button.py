from turtle import width
import numpy as np
from tkinter import *

root=Tk()

root.geometry("600x400")
root.maxsize(550,450)
root.title("Play with quadratic function")

def solve():
    x=x_value.get()
    a=a_value.get()
    b=b_value.get()
    c=c_value.get()
    f=a*x**2+b*x+c
    fx.set(f)
    

def roots():
    a=a_value.get()
    b=b_value.get()
    c=c_value.get()
    root1=(-b+np.lib.scimath.sqrt(b**2-(4*a*c)))/2*a
    root2=(-b-np.lib.scimath.sqrt(b**2-(4*a*c)))/2*a
    r1.set("{: .2f}".format(root1))
    r2.set("{: .2f}".format(root2))

def reset():
    x_value.set(0)
    a_value.set(0)
    b_value.set(0)
    c_value.set(0)
    fx.set(0)
    r1.set(0.0)
    r2.set(0.0)



Label(root, text="f(x) = ax^2+bx+c", font="comicsans 15 bold ", pady=5).grid(columnspan=5)
Label( text="Enter the value : ", font="comicsans 12 bold ").grid(row=1,column=0)
Label( text="x : ",  font="comicsans 15").grid()
Label( text="a : " ,  font="comicsans 15").grid()
Label( text="b : " ,  font="comicsans 15").grid()
Label( text="c : " ,  font="comicsans 15").grid()
 

x_value=IntVar( value=None)
Entry( textvariable=x_value).place(x=150, y=70)
a_value=IntVar()
Entry( textvariable=a_value).place(x=150, y=100)
b_value=IntVar()
Entry( textvariable=b_value).place(x=150, y=130)
c_value=IntVar()
Entry( textvariable=c_value).place(x=150, y=160)


f=Frame(root ,pady=20)
f.grid(row=6, )

Button( text="Solve for x", font="comicsans 10", relief=RAISED, command=solve).place( x=60, y=210)
Button( text="Find roots", font="comicsans 10", relief=RAISED, command=roots).place( x=160, y=210)
Button(text="Reset",relief=RAISED, font="comicsans 10", command=reset).place( x=260, y=210)


fx=IntVar()
Label(text="Value of function f is ", font="comicsans 12 bold ").place( x=26, y=260)
Label(padx=18, pady=18, borderwidth=1, relief=SUNKEN, textvariable=fx).place( x=250, y=260)


r1=DoubleVar()
r2=DoubleVar()
Label(text="Roots of equation f(x) = 0 :", font="comicsans 12 bold ").place( x=26, y=320)
Label(padx=15, pady=15, borderwidth=1, relief=SUNKEN, textvariable=r1).place( x=250, y=320)
Label(text="and            ",).place( x=360, y=330)
Label(padx=15, pady=15, borderwidth=1, relief=SUNKEN, textvariable=r2).place( x=420, y=320)
  

root.mainloop()