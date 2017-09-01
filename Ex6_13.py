import math as m
from pylab import plot,show
from numpy import arange

def f(x):
    return 5*m.exp(-x) + x - 5

def getRoot(x1,x2,epsilon):
    #check that f(x1) and f(x2) have opposite signs
    sign = f(x1)*f(x2)
    if sign > 0:
        return ValueError("f(x1) and f(x2) must be opposite sign")

    #Calculate midpoint between two guesses
    while True:
        x = (x1+x2)/2.0
        #if f(x1) has same sign as f(x), set x1 = x. Otherwise x2 = x
        if f(x)*f(x1) > 0:
            x1 = x
        else:
            x2 = x

        #if |x1 - x2| > target accuracy, repeat. Otherwise, evaluate mid-point
        #once more and return it.
        if abs(x1-x2) < epsilon:
            x = (x1+x2)/2.0
            break
    return x
x1,x2 = 4,6
epsilon = 1E-6
x = getRoot(x1,x2,epsilon)
h = 6.63E-34
c = 2.9999E8
k = 1.38E-23
b = h*c/(k*x)
print b

#c)
wav = 502E-9
Tsun = b/wav
print Tsun
        
        
        

    
        
    
    
    
