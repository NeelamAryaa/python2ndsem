# ques-1
import math
import numpy as np
def h(x):
    return (1/math.sqrt(2*math.pi))*np.exp((-1/2)*x**2)

# print(h(3))    
x=np.linspace(-5,5,51)
print(h(x))

