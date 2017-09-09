import numpy as np
from pylab import plot,show

def f(x,r):
    y,yprime = r
    fx = yprime
    fxx = -0.1*yprime - x
    return np.array([fx,fxx],float)
    
def analytical(x):
    return x*(100 - 5*x) + 990*(np.exp(-0.1*x) - 1)

def integrate(f,x,r,xStop,h):
    ''' X,Y = euler(f,x,y,xStop,h)
    Euler method for solving the
    intial value problem {y}' = {f(x,y)} where
    {y} = {y[0],...y[n-1]}
    x,y = intial conditions
    xStop = terminal value of x
    h = increment of x used in integration
    f = user-defined function'''

    def rk4(f,x,r,h):
        k1 = h*f(x,r)
        k2 = h*f(x + 0.5*h, r + 0.5*k1)
        k3 = h*f(x + 0.5*h, r + 0.5*k2)
        k4 = h*f(x + h, r + k3)
        return (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0

    X = []
    Y = []
    while x < xStop:
        X.append(x)
        y,yprime = r
        Y.append(y)
        h = min(h,xStop - x)
        r += rk4(f,x,r,h)
        x += h
    return np.array(X),np.array(Y)

x = 0.0
xStop = 2.0
h = 0.2
y = np.array([0.0,1.0],float)
X,Y = integrate(f,x,y,xStop,h)
plot(X,Y,'o',X,analytical(X))
show()
