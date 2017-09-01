from numpy import array, arange,pi

x0 = 0.0
xL = 5.2918E-11
e = 1.6022E-19
E1 = 0.0
E2 = e
target = e/1000

def V(x):
    V0 = 100*e
    return V0*(x/xL)*(x/xL - 1)

def f(r,x,E):
    #parse vector
    psi,phi = r
    #constants
    hbar = 6.63E-34/(2*pi)
    m = 9.1094E-31
    #calculate the first and second order derivatives
    fpsi = phi
    fphi = 2*m*psi*(V(x) - E)/hbar**2
    return array([fpsi,fphi],float)

def EigenValue(a,b,E):

    #runge-kutta function
    def rk4(r,x,h):
        k1 = h*f(r,x,E)
        k2 = h*f(r + 0.5*k1,x + 0.5*h,E)
        k3 = h*f(r + 0.5*k2,x + 0.5*h,E)
        k4 = h*f(r + k3,x + h,E)
        return (k1 + 2*(k2 + k3) + k4)/6.0

    #initial conditions
    psi,phi = 0.0,1.0
    r = array([psi,phi],float)
    N = 1000
    h = abs(a-b)/N
    #obtain the solution from runge-kutta and return end value
    for x in arange(a,b,h):
        r += rk4(r,x,h)
    psi,phi = r
    return psi


psi2 = EigenValue(x0,xL,E1)
while abs(E1 - E2) > target:
    psi1,psi2 = psi2,EigenValue(x0,xL,E2)
    E1,E2 = E2,E2 - psi2*(E2 - E1)/(psi2 - psi1)

print "E = ",E2/e,"eV"





 
