from pylab import plot,show,legend,axvline
from numpy import arange,sin,linspace

def f(x,t):
    return -x**3 + sin(t)

def AdaptiveRK4(f,a,b,x,h):

    def RK4(h,x,t):
        k1 = h*f(x,t)
        k2 = h*f(x + k1*0.5, t + h*0.5)
        k3 = h*f(x + k2*0.5, t + h*0.5)
        k4 = h*f(x + k3, t + h) 
        return (k1 + 2*(k2 + k3) + k4)/6

    def adaptiveStep(h,x,t,sig = 1e-6):
        x1 = x + RK4(h,x,t)
        x1 += RK4(h,x1,t+h)
        x2 = x + RK4(2*h,x,t)

        eps = 30.0/abs(x1-x2)
        target = h*sig
        rho = target*eps
        hprime = h*rho**(1/4.0)
        
        if abs(hprime) > 2*abs(h): hprime = 2*h
        elif abs(hprime) < 0.1*abs(h): hprime = 0.1*h
        
        if rho >= 1.0:
            return hprime,x1
        else:
            return adaptiveStep(hprime,x,t)
    
    t = a
    time = []
    soln = []
    while(t < b):
        soln.append(x)
        time.append(t)
        h,x = adaptiveStep(h,x,t)
        t += h
    return time,soln

h = 0.01
a = 0.0
b = 10
x = 0.0
T,X = AdaptiveRK4(f,a,b,x,h)
plot(T,X,'-')
for i in range(len(T)):
    try:
        axvline(x=T[i*10], ls='dotted')
    except IndexError:
        break
show()
