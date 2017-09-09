from numpy import arange, tanh, cosh, array
from pylab import plot, show, figure

##Forward difference: (f(x+h) - f(x))/h
def forward_diff(f,x,h):
    return (f(x+h) - f(x))/h

##central difference: (f(x+h) - (f(x-h))/2h
def central_diff(f,x,h):
    return (f(x+h/2) - f(x-h/2))/(h)

f = lambda x: x**2
H = array([10.0**(-a) for a in range(0,16,2)],float)
x = 1.0	
centralDiff = [central_diff(f,x,h) for h in H]
forwardDiff = [foward_diff(f,x,h) for h in H]
print H
plot(H,centralDiff)
plot(H,forwardDiff)
show()