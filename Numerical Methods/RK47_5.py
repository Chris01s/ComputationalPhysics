import numpy as np
from pylab import plot,show

def f(x,y):
    return 3*y - 4*np.exp(-x)

def analytical(x):
    return np.exp(-x)

def integrate(f,x,y,xStop,h):
    ''' X,Y = euler(f,x,y,xStop,h)
    Euler method for solving the
    intial value problem {y}' = {f(x,y)} where
    {y} = {y[0],...y[n-1]}
    x,y = intial conditions
    xStop = terminal value of x
    h = increment of x used in integration
    f = user-defined function'''

    def rk4(f,x,y,h):
        k1 = h*f(x,y)
        k2 = h*f(x + 0.5*h, y + 0.5*k1)
        k3 = h*f(x + 0.5*h, y + 0.5*k2)
        k4 = h*f(x + h, y + k3)
        return (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0

    X = []
    Y = []
    while x < xStop:
        X.append(x)
        Y.append(y)
        h = min(h,xStop - x)
        y += rk4(f,x,y,h)
        x += h
    return np.array(X),np.array(Y)

x = 0.0
xStop = 10.0
h = 0.1
y = 1.0
X,Y = integrate(f,x,y,xStop,h)
for i in range(len(X)-20):
    try:
        print X[i*20],Y[i*20]
    except IndexError:
        break

#plot(X,Y,'o',X,analytical(X))
#show()
