from pylab import plot,show,legend
from numpy import arange,array


def g(x,u):
    return 1/((x*(1-u))**2 + u**2)

def RK4(N):
    h = abs(0 - 1.0)/N
    U = arange(0,1,h,float) 
    soln = []
    x = 1.0
    for u in U:
        soln.append(x)
        k1 = h*g(x,u)
        k2 = h*g(x + 0.5*k1,u + 0.5*h)
        k3 = h*g(x + 0.5*k2,u + 0.5*h)
        k4 = h*g(x + k3,u + h)
        x += (k1 + 2*(k2+k3) + k4)/6
    t = U/(1-U)
    plot(t,soln)
    return soln


N = 100
soln = RK4(N)
show()

