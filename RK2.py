from pylab import plot,show
from numpy import arange,sin

def f(x,t):
    return -x**3 + sin(t)

def RK2(f,N):
    h = abs(0 - 10.0)/N
    time = arange(0,10,h)
    soln = []
    x = 0.0
    for t in time:
        soln.append(x)
        k1 = h*f(x,t)
        k2 = h*f(x + k1*0.5, t + h*0.5)
        x += k2
    plot(time,soln)
    show()
    return soln

N = [10,20,50,100]
for n in N:
    RK2(f,n)
