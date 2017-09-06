from numpy import array
from pylab import plot,show

def f(r,t):
    x,v = r
    fx = v
    fxx = fx**2 - x - 5
    return array([fx,fxx],float)

def Leapfrog(r,t,tStop,h):
    X = []
    T = []
    V = []
    r_halfstep = r + h*f(r,t)/2
    while(t < tStop):
        x,v = r
        X.append(x)
        V.append(v)
        T.append(t)
        
        r += h*f(r_halfstep,t + h/2)
        r_halfstep += h*f(r,t + h)
        t += h
    return array(T),array(X),array(V)
    
a = 0
b = 50.0
h = 1e-3
r = array([1.0,0.0],float)
T,X,V = Leapfrog(r,a,b,h)
plot(X,V)
show()
