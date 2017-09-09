import numpy as np
from rk5 import*
from pylab import plot,show,legend,grid


def f(t,r):
    '''This function returns a vector of the simultaneous
    multivariable equations the arguments are a vector, r,
    and t the independent variable'''
    #parse the vector 
    theta,omega = r
    #set up intial conditions
    g = 9.81
    l = 0.1
    #calculate values from respective functions
    ftheta = omega
    fomega = -g*np.sin(theta)/l
    #return the results as a vector 
    return np.array([ftheta,fomega],float)

t = 0.0
tStop = 10.0
N = 100
h = abs(t-tStop)/N
omega = np.array([179*np.pi/180,0.0],float)
T,O = integrate(f,t,omega,tStop,h,1e-4)
plot(T,O[:,1],'o-')
show()
