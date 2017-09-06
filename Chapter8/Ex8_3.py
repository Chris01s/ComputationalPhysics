from pylab import plot,show,legend,figure
from numpy import arange,array,sin
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def f(r,t):
    '''This function returns a vector of the simultaneous
    multivariable equations the arguments are a vector, r,
    and t the independent variable'''
    #parse the vector 
    x,y,z = r
    #set up intial conditions
    a = 28
    b = 8/3
    sigma = 10
    #calculate values from respective functions
    fx = sigma*(y - x)
    fy = (a - z)*x - y
    fz = x*y - b*z
    #return the results as a vector 
    return array([fx,fy,fz],float)

def RK4(a,b,N):
    #set up initial conditions
    h = abs(a - b)/N
    xsoln = []
    ysoln = []
    zsoln = []
    time = arange(a,b,h,float) 
    r = array([0,1,0],float)
    for t in time:
        #parse the vector, and append to respective lists
        x,y,z = r
        xsoln.append(x)
        ysoln.append(y)
        zsoln.append(z)
        #do Runge Kutta calculation on the vector r
        k1 = h*f(r,t)
        k2 = h*f(r + 0.5*k1,t + 0.5*h)
        k3 = h*f(r + 0.5*k2,t + 0.5*h)
        k4 = h*f(r + k3,t + h)
        r += (k1 + 2*(k2+k3) + k4)/6
    return time,xsoln,ysoln,zsoln

N = 10000
a = 0.0
b = 100.0
time, xsoln, ysoln, zsoln = RK4(a,b,N)
#a)
#plot results
figure(1)
plot(time,ysoln)
#b)
#3D plot is much better for the strange attractor
fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
ax.plot_wireframe(xsoln,ysoln,zsoln)
show()
