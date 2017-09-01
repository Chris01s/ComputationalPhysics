from pylab import plot,show,legend,ylim,xlim,xlabel,ylabel
from numpy import arange,tan,sqrt,pi,array

#constants
q = 1.6E-19
m = 9.11E-31
w = 10E-10
hbar = 6.63E-34/(2*pi)

def f1(V,E):
    return tan(w*sqrt(2*m*E)/(2.0*hbar)) - sqrt((V-E)/E)

def f2(V,E):
    return tan(w*sqrt(2*m*E)/(2.0*hbar)) + sqrt(E/(V-E))

def Bisection(f,V,E1,E2,epsilon):
    #check that f(x1) and f(x2) have opposite signs
    sign = f(V,E1)*f(V,E2)
    if sign > 0:
        return ValueError("f(x1) and f(x2) must be opposite sign")
    #Calculate midpoint between two guesses
    while True:
        E = (E1+E2)/2.0
        #if f(x1) has same sign as f(x), set x1 = x. Otherwise x2 = x
        if f(V,E)*f(V,E1) > 0:
            E1 = E
        else:
            E2 = E
        #if |x1 - x2| > target accuracy, repeat. Otherwise, evaluate mid-point
        #once more and return it.
        if abs((E1-E2)/q) < epsilon:
            E = (E1+E2)/2.0
            break
    return E/q

#a)
#constants
E = arange(0,20,0.001)*q
V = 20*q

#functions
kappa = sqrt(2*m*(V-E))/hbar
k = sqrt(2*m*E)/hbar

y1 = tan(k*w/2.0)
y2 = kappa/k #for even solutions
y3 = -1/y2 #for odd solutions
#plots to examine where solutions are: intersections 
plot(E/q,y1,'--',label=r'$\tan(kL/2)$') 
plot(E/q,y2,label=r'$\frac{\kappa}{k}$:even solns')
plot(E/q,y3,label=r'$\frac{-k}{\kappa}$:odd solns')
legend(loc='upperright')
ylim(-8,8)
xlim(0.0,20)
xlabel('E(eV)')
ylabel(r'$\tan(kL/2)$')


#b)
#even solutions
epsilon = 1E-5
#eyeball the graph above and find starting positions for the bisection method
E1 = [2,7,14]
E2 = [3,9,16]
evenSolns = array([Bisection(f1,V,e1*q,e2*q,epsilon) for e1,e2 in zip(E1,E2)])
k_even = sqrt(2*m*evenSolns*q)/hbar
#odd solutions: same as above
E1 = [0.5,4,10]
E2 = [1.5,6,12]
oddSolns = array([Bisection(f2,V,e1*q,e2*q,epsilon) for e1,e2 in zip(E1,E2)])
k_odd = sqrt(2*m*oddSolns*q)/hbar
plot(evenSolns,tan(k_even*w/2),'o')
plot(oddSolns,tan(k_odd*w/2),'o')
show()
