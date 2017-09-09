import numpy as np

def func(x,y):
    return np.sin(y)

def integrate(f,x,y,xStop,h):
    ''' X,Y = euler(f,x,y,xStop,h)
    Euler method for solving the
    intial value problem {y}' = {f(x,y)} where
    {y} = {y[0],...y[n-1]}
    x,y = intial conditions
    xStop = terminal value of x
    h = increment of x used in integration
    f = user-defined function'''

    def rk2(f,x,y,h):
        k0 = h*f(x,y)
        k1 = h*f(x + 0.5*h, y + 0.5*k0)
        print k0,k1
        return k1

    X = []
    Y = []
    while x < xStop:
        X.append(x)
        Y.append(y)
        #h = min(h,xStop - x)
        y += rk2(f,x,y,h)
        x += h
    return np.array(X),np.array(Y)

x = 0.0
xStop = 0.5
h = 0.1
y = 1.0
X,Y = integrate(func,x,y,xStop,h)
