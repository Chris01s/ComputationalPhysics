import math as m

def V(sig,r):
    return (sig/r)**6 - m.exp(-r/sig)

def GoldenSearch(f,sig,x1,x4,epsilon):
    z = (1+m.sqrt(5))/2
    #Calculate interior values based on Golden ratio
    x2 = x4 - (x4 - x1)/z
    x3 = x1 + (x4 - x1)/z
    f1,f2,f3,f4 = f(sig,x1),f(sig,x2),f(sig,x3),f(sig,x4)
    while True:
        if f2 < f3:
            x4,f4 = x3,f3
            x3,f3 = x2,f2
            x2 = x4 - (x4 - x1)/z
            f2 = f(sig,x2)
        else:
            x1,f1 = x2,f2
            x2,f2 = x3,f3
            x3 = x1 + (x4 - x1)/z
            f3 = f(sig,x3)
        if abs(x4-x1) < epsilon:
            x2 = (x1 + x4)/2.0
            break
    return x2

epsilon = 1e-6
sig = 1.0
x1, x4 = sig/10,sig*10
Vmin = GoldenSearch(V,sig,x1,x4,epsilon)
print "The minimum falls on",Vmin,"nm"
