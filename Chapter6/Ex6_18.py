import numpy as np
import pylab as py
import sys
sys.path.append('C:\Users\CHRIS\Documents\Python Scripts\LearningScripts\ComputationalPhysicsExercises\ExamplesAndUseful')
from gaussxw import gaussxw

def func(x):
    return x**3 / (np.exp(x) - 1)

def neta(f,x,w,gamma1,gamma2,T):
    N = 100
    s = 0.0
    xp = 0.5*(x*(gamma1-gamma2)/T + (gamma1+gamma2)/T)
    wp = 0.5*w*(gamma1-gamma2)/T
    for i in range(N):
        s += f(xp[i])*wp[i]
    return s*15/np.pi**4

def minNeta(T):
    return -neta(func,x,w,gamma1,gamma2,T)

def GoldenSearch(f,x1,x4,epsilon):
    z = (1 + np.sqrt(5))/2
    #Calculate interior values based on Golden ratio
    x2 = x4 - (x4 - x1)/z
    x3 = x1 + (x4 - x1)/z
    f1,f2,f3,f4 = f(x1),f(x2),f(x3),f(x4)
    while True:
        if f2 < f3:
            x4,f4 = x3,f3
            x3,f3 = x2,f2
            x2 = x4 - (x4 - x1)/z
            f2 = f(x2)
        else:
            x1,f1 = x2,f2
            x2,f2 = x3,f3
            x3 = x1 + (x4 - x1)/z
            f3 = f(x3)
        print x2
        if abs(x4-x1) < epsilon:
            x2 = (x1 + x4)/2.0
            break
    return x2, f(x2)


#a)
#fundamental constants
c = 2.99792458E8
h = 6.62607004E-34
k = 1.38064852E-23
#limits    
wav1, wav2 = 390E-9, 750E-9
gamma1 = h*c/(k*wav1)
gamma2 = h*c/(k*wav2)
#sample points and weights for Gaussian integration
N = 100
x,w = gaussxw(N)
T = np.arange(300,10E3,1)
Neta = [neta(func,x,w,gamma1,gamma2,Tn) for Tn in T]
py.plot(T,Neta)
py.show()


#b)
x1,x4 = 300,10E3
epsilon = 1e-6
maxNeta = GoldenSearch(minNeta,x1,x4,epsilon)
print maxNeta




