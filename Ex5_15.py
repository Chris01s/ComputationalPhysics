from numpy import linspace, tanh, cosh, array, arange, zeros
from pylab import plot, show, figure

##Forward difference: (f(x+h) - f(x))/h
def forward_diff(f,x,h):
    return (f(x+h) - f(x))/h

f = lambda x: 1 + 0.5*tanh(2*x)
x = linspace(-2,2,100,endpoint=True)
h = 1E-3

##central difference: (f(x+h) - (f(x-h))/2h
def central_diff(f,x,h):
    return (f(x+h/2) - f(x-h/2))/h
	
fprime = central_diff(f,x,h)

figure(1)
plot(x,fprime,'.', x, 1/cosh(2*x)**2)
show()
