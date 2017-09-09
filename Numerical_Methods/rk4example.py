import math
import numpy as np
from pylab import plot,show
from rk5 import*


def f(x,t):
    return -x**3 + np.sin(t)

a = 0.0
b = 10.0
N = 1000
h = abs(a-b)/N
x = np.array([0.0])
T,X = integrate(f,a,x,b,h)
plot(T,X,'o')
show()
