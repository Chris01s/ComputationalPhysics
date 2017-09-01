from numpy import arange, tanh, cosh, array,log10
from pylab import plot, show, figure

##Forward difference: (f(x+h) - f(x))/h
def forward_diff(f,x,h):
    return (f(x+h) - f(x))/h

##central difference: (f(x+h) - (f(x-h))/2h
def central_diff(f,x,h):
    return (f(x+h/2) - f(x-h/2))/(h)

f = lambda x: x**2
h = array([10.0**(-a) for a in range(-10,16)],float)
x = 1	
centralDiff = central_diff(f,x,h)
forwardDiff = forward_diff(f,x,h)

plot(log10(h), (centralDiff-2)/2,'b.', log10(h), (forwardDiff-2)/2,'r.')
show()