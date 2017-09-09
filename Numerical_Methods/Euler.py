import numpy as np

def func(x,y):
    return x*x - 4*y

def analytical(x):
    return 31/32.0*np.exp(-4*x) + 0.25*x*(x - 0.5) + 1/32.0

def euler(f,x,y,xStop,h):
    ''' X,Y = euler(f,x,y,xStop,h)
    Euler method for solving the
    intial value problem {y}' = {f(x,y)} where
    {y} = {y[0],...y[n-1]}
    x,y = intial conditions
    xStop = terminal value of x
    h = increment of x used in integration
    f = user-defined function           '''

    X = []
    Y = []
    while x < xStop:
        X.append(x)
        Y.append(y)
        h = min(h,xStop - x)
        y += h*f(x,y)
        x += h
        Eacc = y - analytical(x)
        print Eacc
    return np.array(X),np.array(Y)

x = 0.0
y = 1.0
xStop = 0.03
h = 0.01
X,Y = euler(func,x,y,xStop,h)


        
