from numpy import array,sqrt,transpose
from pylab import plot,show,figure


def f(r,t):
    #calculate second order derivatives
    R = sqrt(sum(r**2))
    frr = -G*M*r/R**3
    return frr

def Verlet(r,v,t,tStop,h):
    X = []
    Y = []
    Vsq = []
    R = []
    vhalf = v + h*f(r,t)/2
    while(t < tStop):
        #append to lists
        x,y = r
        X.append(x); Y.append(y)
        Vsq.append(sum(v**2)); R.append(sqrt(sum(r**2)))
        
        #full time step calculation
        r += h*vhalf
        k = h*f(r,t+h)
        v += k/2
        
        #next half step
        vhalf += k
        t += h
    return array(X),array(Y),array(Vsq),array(R)

#constants
G = 6.6738E-11
M = 1.9891E30
AU = 1.4710E11
m = 5.9722E24
#initial conditions
t = 0.0
tStop = 7*365.65*24*3600
h = 3600.0
r = array([AU,0.0],float)
v = array([0.0,3.0287E4],float)

#calculate using verlet
X,Y,Vsq,R = Verlet(r,v,t,tStop,h)

PE = -G*M*m/R
KE = 0.5*m*Vsq
E = KE + PE

#plot graphs
figure(1)
plot(E,'o',KE,'--',PE,'-')
figure(2)
plot(X,Y)
show()

        
        
