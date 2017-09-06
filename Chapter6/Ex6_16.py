from numpy import linspace,array,pi
from pylab import plot,show

G = 6.674E-11
m = 5.974E24
M = 1.9899E30
R = 1.498E11
w = 2*pi/(3600*24*365)

def f(r):
    return G*(M/(r**2.0) - m/((R-r)**2.0)) - r*w**2.0

def fprime(r):
    return -(2*G*(M/(r**3.0) + m/((R-r)**3.0)) + w**2.0)

def Newt(r,acc):
    while True:
        delta = f(r)/fprime(r)
        r -= delta
        if abs(delta/R) < acc:
            break
    return r

def Secant(r1,r2,acc):
    while True:
        r1, r2 = r2 - f(r2)*(r2 - r1)/(f(r2) - f(r1)), r1
        delta = r1 - r2
        if abs(delta) < acc:
            break
    return r1

acc = 1E-12
r = 1.0

##Test for different systems
soln = Newt(r,acc)
print "Earth-Sun L1 point is around:", soln/R

M = 5.974E24
m = 7.438E22
R = 3.844E8
w = 2.662E-6
soln = Newt(r,acc)
print "Earth-Moon L1 point is around:", soln/R


r1,r2 = 1,2
solnSecant = Secant(r1,r2,acc)
print solnSecant/R
