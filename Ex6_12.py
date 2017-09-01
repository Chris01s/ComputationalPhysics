import math as m
from pylab import plot,show
from numpy import arange

def relax(x1,y1):
    a,b = 1,2
    def f1(a,x,y):
        return (a + x**2)*y

    def f2(a,b,x):
        return b/(a + x**2)

    def epsilon(x,xprime):
        return abs((x - xprime)/xprime)
    
    acc = 1E-10
    while True:
        y1, y2 = f2(a,b,x1),y1
        x1, x2 = f1(a,x1,y1),x1
        if epsilon(x1,x2) < acc and epsilon(y1,y2) < acc:
            break
    return x1,y1

x = 50.0
y = 10.0
x,y = relax(x,y)
print x,y
