import math as m
from pylab import plot,show
from numpy import arange


def f(x):
    return 20*x**3 + 30*x**2 - 10*x
def fprime(x):
    return 60*(x**2 + x) - 10
def f2prime(x):
    return 60*(2*x + 1)

def GoldenSearch(f,x1,x4,epsilon):
    z = (1+m.sqrt(5))/2
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
        if abs(x4-x1) < epsilon:
            x2 = (x1 + x4)/2.0
            break
    return x2

def Newt(x,acc):
    while True:
        delta = fprime(x)/f2prime(x)
        print 1/f2prime(x)
        x -= delta
        if abs(delta) < acc:
            break
    return x

def Secant(x1,x2,acc,gamma):
    while True:
        x1, x2 = x2 - gamma*(f(x2) - f(x1))/(x2 - x1), x1
        delta = x1 - x2
        print x1
        if abs(delta) < acc:
            break
    return x1


        
#Choose intial values and set tolerance level
epsilon = 1e-6
x1,x4 = -2,1
#Calculate min
Goldenmin = GoldenSearch(f,x1,x4,epsilon)
Newtonmin = Newt(1.0,epsilon)
#Secantmin = Secant(-1.0,-0.9,epsilon,0.01)
#plot results

x = arange(-2,1,0.01)
plot(x,f(x))
plot(Goldenmin,f(Goldenmin),'o')
show()

