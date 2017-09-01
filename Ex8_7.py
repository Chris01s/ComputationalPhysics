from pylab import plot,show,legend,figure
from numpy import arange,array,sin,cos,pi,sqrt

def f(r,t,m):
    #parse the function vector
    x,y,vx,vy = r
    #intial conditions
    C = 0.47
    R = 0.08
    rho = 1.22
    g = 9.81
    alpha = pi*R**2*rho*C/(2*m)
    #calculate the derivatives
    fx,fy = vx,vy
    fxx = -alpha*vx*sqrt(vx**2 + vy**2)
    fyy = -alpha*vy*sqrt(vx**2 + vy**2) - g
    return array([fx,fy,fxx,fyy],float)

def g(r,t,m):
    #parse the function vector
    x,y,vx,vy = r
    #intial conditions
    g = 9.81
    #calculate the derivatives
    fx,fy = vx,vy
    fxx = 0
    fyy = -g
    return array([fx,fy,fxx,fyy],float)
    

def RK4(f,a,b,N,m):
    #set up initial conditions
    h = abs(a - b)/N
    rad = pi/180
    vx,vy = 100*array([cos(30*rad),sin(30*rad)])
    xsoln = []
    ysoln = []
    time = arange(a,b,h,float) 
    r = array([0,0,vx,vy],float)
    for t in time:
        #parse the vector, and append to respective lists
        x,y,vx,vy = r
        xsoln.append(x)
        ysoln.append(y)
        #do Runge Kutta calculation on the vector r
        k1 = h*f(r,t,m)
        k2 = h*f(r + 0.5*k1,t + 0.5*h,m)
        k3 = h*f(r + 0.5*k2,t + 0.5*h,m)
        k4 = h*f(r + k3,t + h,m)
        r += (k1 + 2*(k2+k3) + k4)/6
    plot(xsoln,ysoln,label=r'm=%d'%(m))
    return xsoln,ysoln

#b)Resistance
a = 0.0
b = 10
N = 1000
m = 1
##x,y = RK4(f,a,b,N,m)
##plot(x,y)
###No resistance
##x,y = RK4(g,a,b,N,m)
##plot(x,y)
###b)
masses = array([1,2,5,10],float)
solns = [RK4(f,a,b,N,m) for m in masses]
legend(loc='upper right')
show()


