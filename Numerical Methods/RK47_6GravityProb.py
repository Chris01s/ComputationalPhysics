import numpy as np
from pylab import plot,show

def f(t,y):
    #parse the input vector
    r,dr,theta,dtheta = y
    #constants
    G = 6.67E-11
    Me = 5.9742E24
    #calculate the 
    Fr = dr
    Frr = r*dtheta**2 - G*Me/r**2
    Ftheta = dtheta
    Fthetatheta = -2*dr*dtheta/r
    return np.array([Fr,Frr,Ftheta,Fthetatheta],float)

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
    R = []
    while x < xStop:
        X.append(x)
        R.append(r)
        h = min(h,xStop - x)
        r += rk4(f,x,r,h)
        x += h
    return np.array(X),np.array(R)

Re = 6378.14E3
H = 772E3
v0 = 6700.0
t = 0.0
tStop = 1200.0
h = 50.0
y = np.array([Re+H, 0, 0, v0/(Re+H)],float)
X,Y = integrate(f,t,y,tStop,h)
for i in range(len(X)):
    try:
        print X[i*2],Y[i*2]
    except IndexError:
        break








