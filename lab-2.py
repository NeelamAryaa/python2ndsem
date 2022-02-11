# ques-1

# ques 2
# def n_fib_prime(n):


# ques-3
def twos(rows,cols):
    arr = [[2 for col in range(cols)] for row in range(rows)]
    return arr

m=int(input("no. of rows"))
n=int(input("no. of cols"))
print(twos(m,n))


# ques-4
from matplotlib.cbook import index_of
import numpy as np
def with_tolerance(A,a,tol):
    a=abs(A-a)
    for i in a:
        if(i<tol):
            arr=[]
            arr.append(a.index(i))
    return arr

A=np.array([0.0,1.0,2.0,3.0])
a=1.5
tol=0.75

with_tolerance(A,a,tol)

