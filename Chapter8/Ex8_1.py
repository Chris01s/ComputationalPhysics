from pylab import plot,show,legend
from numpy import arange,array

def Vin(t):
    if int(2*t)%2 == 0:
        return 1.0
    else:
        return -1.0

def dVout(Vout,t,RC):
    return (Vin(t) - Vout)/RC

def RK4(f,RC,N):
    h = abs(0 - 10.0)/N
    time = arange(0,10,h,float)
    soln = []
    Vout = 0.0
    for t in time:
        soln.append(Vout)
        k1 = h*f(Vout,t,RC)
        k2 = h*f(Vout + 0.5*k1,t + 0.5*h,RC)
        k3 = h*f(Vout + 0.5*k2,t + 0.5*h,RC)
        k4 = h*f(Vout + k3,t + h,RC)
        Vout += (k1 + 2*(k2+k3) + k4)/6
    plot(time,soln,label=r'RC=%f'%(RC))
    return soln

RC = array([0.01,0.1,1.0])
N = 1000
for rc in RC:
    RK4(dVout,rc,N)
legend(loc='upper right')
show()
