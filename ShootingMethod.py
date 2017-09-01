from numpy import arange,array

def f(r,t):
    #parse input vector
    x,v = r
    #constants
    g = 9.81
    #calculate first derivatives
    fx = v
    fv = -g
    return array([fx,fv],float)

def height(v):
    
    def rk4(r,t,h):
        k1 = h*f(r,t)
        k2 = h*f(r + 0.5*k1,t + 0.5*h)
        k3 = h*f(r + 0.5*k2,t + 0.5*h)
        k4 = h*f(r + k3,t + h)
        return (k1 + 2*(k2 + k3) + k4)/6.0

    r = array([0.0,v],float)
    a = 0.0
    b = 10.0
    N = 1000
    h = abs(a-b)/N
    time = arange(a,b,h)
    for t in time:
        r += rk4(r,t,h)
    x,v = r
    return x

v1,v2 = 0.01,1000.0
h1, h2 = height(v1),height(v2)
target = 1e-10
while abs(h2 - h1) > target:
    vp = (v1 + v2)/2
    hp = height(vp)
    if(hp*h1) > 0:
        v1 = vp
        h1 = hp
    else:
        v2 = vp
        h2 = hp 

v = (v1 + v2)/2
print v
    

    
    
