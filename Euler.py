from pylab import plot,show
from numpy import arange,sin

def f(x,t):
    return -x**3 + sin(t)

N = 4000
h = abs(0 - 10.0)/N
time = arange(0,10,h)
soln = []
x = 0.0
for t in time:
    x += h*f(x,t)
    soln.append(x)
    
plot(time,soln)
show()
