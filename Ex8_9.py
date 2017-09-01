from pylab import plot,show,legend,figure
from numpy import arange,array,zeros,cos,copy

def f(r,t):
    #parse the function vector
    x,v = r
    #intial conditions
    m = 1
    k = 6
    omega = 2
    #calculate the derivatives
    M = len(x)
    fx = zeros(M,float)
    fx[0] = cos(omega*t)
    dx = v
    dxx = zeros(M,float)
    for i in range(M):
        if i == 0:
            dxx[i] = (k*(x[i+1] - x[i]) + fx[i])/m
        elif i == M-1:
            dxx[i] = (k*(x[i-1] - x[i]) + fx[i])/m
        else:
            dxx[i] = (k*(x[i+1] + x[i-1] - 2*x[i]) + fx[i])/m
    return array([dx,dxx],float)

def RK4(f,a,b,N,M):
    #set up initial conditions
    xsoln = []
    x = zeros(M,float)
    v = zeros(M,float)
    r = array([x,v],float)
    #calculate step size and time array
    h = abs(a - b)/N
    time = arange(a,b,h,float)
    for t in time:
        #parse the vector, and append to respective lists
        x,v = r.copy()
        xsoln.append(x)
        #do Runge Kutta calculation on the vector r
        k1 = h*f(r, t)
        k2 = h*f(r + 0.5*k1, t + 0.5*h)
        k3 = h*f(r + 0.5*k2, t + 0.5*h)
        k4 = h*f(r + k3, t + h)
        r += (k1 + 2*(k2+k3) + k4)/6
    return time, xsoln

#time interval
a = 0
b = 20.0
#number of points
N = 1000
#number of bodies
M = 5
#perform RungeKutta
time, x = RK4(f,a,b,N,M)
#plot
figure(1)
plot(time,x)    
show()
