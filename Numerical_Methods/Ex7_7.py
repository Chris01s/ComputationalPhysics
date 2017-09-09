import math
import numpy as np
from pylab import plot,show
from rk5 import*


def f(x,r):
    y,v = r
    #const
    a = 7.45
    b = 10.53E-5
    g = 9.80665
    m = 114
     
    Fy = v
    FD = a*math.exp(-b*y)*v**2
    Fyy = -g + FD/m
    return np.array([Fy,Fyy],float)


t = 0.0
tStop = 10
h = 0.5
y = np.array([9000,0.0])
T,Y = integrate(f,t,y,tStop,h,1e-3)
plot(T,Y[:,0])
show()
