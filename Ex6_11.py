import math as m
from pylab import plot,show
from numpy import arange

def relax(c,x1):
    def f(c,x):
        return 1 - m.exp(-c*x)

    def fprime(c,x):
        return c*m.exp(-c*x)

    def epsilon(c,x,xprime):
        return abs((x - xprime)/(1 - 1/fprime(c,x)))
    
    acc = 1E-6
    iterations = 0
    while True:
        x1,x2 = f(c,x1),x1
        if epsilon(c,x1,x2) < acc:
            break
        iterations+=1
    return x1,iterations

def overrelax(c,omega,x1):

    def f(c,x):
        return 1 - m.exp(-c*x)
    
    def fprime(c,x):
        return c*m.exp(-c*x)
    
    def err(c,x1,x2,omega):
        return abs((x1-x2)/(1 - 1/((1 + omega)*fprime(c,x1) - omega)))
    
    acc = 1E-6
    iterations = 0
    while True:
        dx = f(c,x1) - x1
        x1,x2 = x1 + (1 + omega)*dx,x1
        iterations+=1
        if err(c,x1,x2,omega) < acc:
            break
    return x1,iterations

#a)
c = 2
x = 1.0
omega = 0.1
relax(c,x)
overrelax(c,omega,x)


#b)
C = arange(0,3.01,0.01)
N = len(C)
solns = [relax(c,x) for c in C]
plot(C,solns)
show()

#c)
print [overrelax(c,w,x) 
