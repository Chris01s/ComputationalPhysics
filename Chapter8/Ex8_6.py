from pylab import plot,show,legend,figure
from numpy import arange,array

def f(r,t):
    #initial conditions
    x,velocity = r
    omega = 1
    #calculations
    fx = velocity
    fxx = -x*omega**2
    return array([fx,fxx],float)

def g(r,t):
    #initial conditions
    x,velocity = r
    omega = 1
    #calculations
    fx = velocity
    fxx = -x*(x*omega)**2
    return array([fx,fxx],float)

def VDP(r,t):
    #intial conditions
    x,velocity = r
    omega = 1
    mu = 4
    #calculations
    fx = velocity
    fxx = +mu*(1-x**2)*velocity - x*omega**2
    return array([fx,fxx],float)

def RK4(f,a,b,N):
    #set up initial conditions
    h = abs(a - b)/N
    xsoln = []
    vsoln = []
    time = arange(a,b,h,float) 
    r = array([1,0],float)
    for t in time:
        #parse the vector, and append to respective lists
        x,v = r
        xsoln.append(x)
        vsoln.append(v)
        #do Runge Kutta calculation on the vector r
        k1 = h*f(r,t)
        k2 = h*f(r + 0.5*k1,t + 0.5*h)
        k3 = h*f(r + 0.5*k2,t + 0.5*h)
        k4 = h*f(r + k3,t + h)
        r += (k1 + 2*(k2+k3) + k4)/6
    return time,xsoln,vsoln

#initial conditions
a = 0
b = 50.0
N = 1000
#a,b)
time, xsoln, vsoln = RK4(f,a,b,N)
figure(1)
plot(time,xsoln)
figure(2)
plot(xsoln,vsoln)

#c,d)
time, xsoln,vsoln = RK4(g,a,b,N)
figure(1)
plot(time,xsoln)
figure(2)
plot(xsoln,vsoln)
show()

#e)
a = 0
b = 20.0
N = 1000
time, xsoln,vsoln = RK4(VDP,a,b,N)
figure(1)
plot(time,xsoln)
figure(2)
plot(xsoln,vsoln)
show()
