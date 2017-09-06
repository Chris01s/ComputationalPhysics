from pylab import plot,show,legend,figure
from numpy import arange,array,sin,pi

def f(r,t):
    '''This function returns a vector of the simultaneous
    multivariable equations the arguments are a vector, r,
    and t the independent variable'''
    #parse the vector 
    theta,omega = r
    #set up intial conditions
    g = 9.81
    l = 0.1
    #calculate values from respective functions
    ftheta = omega
    fomega = -g*sin(theta)/l
    #return the results as a vector 
    return array([ftheta,fomega],float)

def RK4(a,b,N):
    #set up initial conditions
    h = abs(a - b)/N
    xsoln = []
    ysoln = []
    time = arange(a,b,h,float) 
    r = array([179*pi/180,0.0],float)
    for t in time:
        #parse the vector, and append to respective lists
        x,y = r
        xsoln.append(x)
        ysoln.append(y)
        #do Runge Kutta calculation on the vector r
        k1 = h*f(r,t)
        k2 = h*f(r + 0.5*k1,t + 0.5*h)
        k3 = h*f(r + 0.5*k2,t + 0.5*h)
        k4 = h*f(r + k3,t + h)
        r += (k1 + 2*(k2+k3) + k4)/6
    return time,xsoln,ysoln

N = 1000
a = 0.0
b = 10
time, theta, omega = RK4(a,b,N)
plot(time,map(lambda x: x*180/pi,theta),'-')
show()




