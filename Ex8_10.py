from pylab import plot,show,legend,figure
from numpy import array,copy,sqrt

def f(r,t):
    #parse the function vector
    x,y,vx,vy = r

    #intial conditions
    M = 1.989E30
    G = 6.67E-11

    #calculate the derivatives
    fx = vx
    fy = vy
    R = sqrt(x**2 + y**2)
    fxx = -G*M*x/R**3
    fyy = -G*M*y/R**3
    return array([fx,fy,fxx,fyy],float)

def RK4(f,t,r,tStop,h):
    X = []
    Y = []
    T = []
    while(t < tStop):
        #parse the vector, and append to respective lists
        x,y,vx,vy = r.copy()
        T.append(t)
        X.append(x)
        Y.append(y)
        #do Runge Kutta calculation on the vector r
        k1 = h*f(r, t)
        k2 = h*f(r + 0.5*k1, t + 0.5*h)
        k3 = h*f(r + 0.5*k2, t + 0.5*h)
        k4 = h*f(r + k3, t + h)
        r += (k1 + 2*(k2+k3) + k4)/6
        t += h 
    return array(X),array(Y)

r = array([4E12,0.0,0.0,500.0],float)
YR = 3600*24*365.0
h = 1E-4*YR
t = 0.0
tStop = 50*YR
x,y = RK4(f,t,r,tStop,h)
AU = 1.4989E11
plot(x/AU,y/AU,'-')
show()
