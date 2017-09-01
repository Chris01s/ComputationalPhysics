from pylab import plot,show
from numpy import arange,ones,exp
import math as m


def relax(c,x1):
    def f(c,x1):
        return 1 - exp(-c*x1)

    def fprime(c,x1):
        return c*exp(-c*x1)

    def epsilon(c,x1,xprime):
        return abs((x1 - xprime)/(1 - 1/fprime(c,x1)))

    acc = 1E-6
    while True:
        x1,x2 = f(c,x1),x1
        delta = epsilon(c,x1,x2)
        if delta < acc:
            break
    return x1

#b)
C = arange(0.0,3.01,0.01)
N = len(C)
x = 1.0
solns = relax(c,x) for c in C]
plot(C,solns)
show()


