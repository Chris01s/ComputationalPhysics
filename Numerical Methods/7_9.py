import numpy as np
from rk5 import*
from pylab import plot,show,legend,grid

def f(x,r):
    y,dy = r

    fy = dy
    fyy = -19/4.0*y - 10*dy
    return np.array([fy,fyy],float)

x = 0.0
xStop = 10.0
h = 0.1
y = np.array([-9.0,0],float)
X,Y = integrate(f,x,y,xStop,h)
plot(X,Y[:,0],'o-',X,Y[:,1],'^-')
grid(True)
show()
