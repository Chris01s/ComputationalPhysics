from pylab import plot,show,legend
from numpy import arange,sin

def f(x,t):
    return -x**3 + sin(t)

def RK4(f,N):
    h = abs(0 - 10.0)/N
    time = arange(0,10,h,float)
    soln = []
    x = 0.0
    for t in time:
        soln.append(x)
        k1 = f(x,t)
        k2 = f(x + k1*0.5, t + h*0.5)
        k3 = f(x + k2*0.5, t + h*0.5)
        k4 = f(x + k3, t + h) 
        x += (k1 + 2*(k2 + k3) + k4)*h/6
    plot(time,soln,label=r'N=%d'%(N))
    return soln

N = [10,20,50,100]
for n in N:
    RK4(f,n)

legend(loc='upper right')
show()
