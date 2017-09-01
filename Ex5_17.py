##Ex 5.17
from numpy import exp, linspace, log, array
from pylab import plot, show, legend, figure
import sys
sys.path.append('C:\Users\CHRIS\Documents\Python Scripts\LearningScripts\ComputationalPhysicsExercises\cpresources')
from gaussxw import gaussxw, gaussxwab


def func1(a,x):
    return (x**(a-1))*exp(-x)

##a)
figure(1)
x = linspace(0,5,100)
for a in range(2,5):
    plot(x,func1(a,x),label="a = %d"%(a))
show()

#c)
def func3(a,z):
    return (z/(1-z))**(a-1) * exp(-(z/(1-z)))/(1-z)**2

#d)
def func2(a,z):
    return exp((a-1)*log((z/(1-z))) - (z/(1-z)))/(1-z)**2

##Gaussian Quad
def gamma(func2,C):
    N = 200
    a = 0.0
    b = 1.0
    x,w = gaussxwab(N,a,b)
    s = 0.0
    for k in range(N):
        s += w[k]*func2(C,x[k])
    return s

def Gamma(func,C):
    a = 0.0
    b = 1.0 - 1E-15
    N = 10000
    Simp = 0
    h = abs(a - b)/N
    for k in range(1, N):
        if k%2 != 0:
            Simp += 4*func(C,a + k*h)
        else:
            Simp += 2*func(C,a + k*h)
    try:
        func(C,b)
    except:
        b -= 1E-18
    try:
        func(C,a)
    except:
        a += 1E-18
    return (func(C,a) + func(C,b) + Simp)*h/3

#f)

res1 = [Gamma(func2,a) for a in (3,6,10)]
res2 = [gamma(func2,a) for a in (3,6,10)]



