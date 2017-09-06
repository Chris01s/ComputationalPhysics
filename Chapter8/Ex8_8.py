from pylab import plot,show,legend,figure
from numpy import arange,array,sin,cos,pi,sqrt

def f(r,t):
    #parse the function vector
    x,y,vx,vy = r
    #intial conditions
    G = 1
    M = 10
    L = 2
    #calculate the derivatives
    r = sqrt(x**2 + y**2)
    d = (sqrt(r**2 + (L/2)**2)*r**2)
    fx,fy = vx,vy
    fxx = -G*M*x/d
    fyy = -G*M*y/d
    return array([fx,fy,fxx,fyy],float)


def RK4(f,a,b,N):
    #set up initial conditions
    xsoln = []
    ysoln = []
    h = abs(a - b)/N
    time = arange(a,b,h,float)
    r = array([1,0,0,1],float)
    for t in time:
        #parse the vector, and append to respective lists
        x,y,vx,vy = r
        xsoln.append(x)
        ysoln.append(y)
        #do Runge Kutta calculation on the vector r
        k1 = h*f(r,t)
        k2 = h*f(r + 0.5*k1,t + 0.5*h)
        k3 = h*f(r + 0.5*k2,t + 0.5*h)
        k4 = h*f(r + k3,t + h)
        r += (k1 + 2*(k2+k3) + k4)/6
    return xsoln,ysoln


a = 0.0
b = 10
N = 1000
x,y = RK4(f,a,b,N)
plot(x,y)
show()
