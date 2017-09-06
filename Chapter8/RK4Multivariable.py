from pylab import plot,show,legend
from numpy import arange,array,sin


def f(r,t):
    '''This function returns a vector of the simultaneous
    multivariable equations the arguments are a vector, r,
    and t the independent variable'''
    #parse the vector to obtain x and y values
    x,y = r
    #calculate values from respective functions
    fx = x*y - x
    fy = y - x*y + sin(t)**2
    #return the results as a vector 
    return array([fx,fy],float)

def RK4(a,b,N):
    #set up initial conditions
    h = abs(a - b)/N
    xsoln = []
    ysoln = []
    time = arange(a,b,h,float) 
    r = array([1.0,1.0],float)
    for t in time:
        #parse vector to obtain x and y values and append to respective lists
        x,y = r
        xsoln.append(x)
        ysoln.append(y)
        #do Runge Kutta calculation on the vector r
        k1 = h*f(r,t)
        k2 = h*f(r + 0.5*k1,t + 0.5*h)
        k3 = h*f(r + 0.5*k2,t + 0.5*h)
        k4 = h*f(r + k3,t + h)
        r += (k1 + 2*(k2+k3) + k4)/6
    #plot results
    plot(time,xsoln)
    plot(time,ysoln)
    return xsoln,ysoln

N = 100
a = 0.0
b = 10.0
RK4(a,b,N)
show()

