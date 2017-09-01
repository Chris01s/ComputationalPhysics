from numpy import linspace,array
from pylab import plot,show

def P(x):
    return (924*x**5 -2772*x**4 + 3150*x**3 - 1680*x**2 + 420*x - 42)*x + 1

def Pprime(x):
    return 6*924*x**5 - 5*2772*x**4 + 4*3150*x**3 - 3*1680*x**2 + 2*420*x - 42

def Newton(x,acc):
    while True:
        delta = (P(x)/Pprime(x))
        x -= delta
        if max(abs(delta)) < acc:
            break
    return x
        
#a)
x = linspace(0,1,100)
plot(x,P(x))

#b)
acc = 1E-10
xguess = array([0.25,0.18,0.35,0.65,0.8,0.95])
roots = Newton(xguess,acc)
xsolns = P(roots)
plot(roots,xsolns,'o')
show()
