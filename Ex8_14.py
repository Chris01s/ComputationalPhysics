from numpy import array, arange,pi,sqrt
from pylab import plot,show,figure

a = 1E-11
x0 = -10*a
xL = 10*a
e = 1.6022E-19
E1 = 0.0
target = e/1000

def V(x):
    '''Function for the potential well:
    x = location in the well
    V0 is the height of the well'''
    V0 = 50*e
    return V0*(x/a)**4


def f(r,x,E):
    '''Schrodinger Wave Equation:
    r = values for the two variables of interest (phi and psi)
    x = location in the well
    E = value for the energy of the quantum state '''
    #parse vector
    psi,phi = r
    #constants
    hbar = 6.63E-34/(2*pi)
    m = 9.1094E-31
    #calculate the first and second order derivatives
    fpsi = phi
    fphi = 2*m*psi*(V(x) - E)/hbar**2
    
    return array([fpsi,fphi],float)


#runge-kutta calculation
def rk4(r,x,h,E):
    '''r = input array for variables of interest
       x = location in the well
       h = step size
       E = value for the energy in the quantum state '''
    k1 = h*f(r,x,E)
    k2 = h*f(r + 0.5*k1,x + 0.5*h,E)
    k3 = h*f(r + 0.5*k2,x + 0.5*h,E)
    k4 = h*f(r + k3,x + h,E)
    return (k1 + 2*(k2 + k3) + k4)/6.0


def wavefunction(a,b,E):
    '''Function to obtain solutions to the quantum well.
        a = lower limit to width of well
        b = upper limit
        E = energy of the quantum state '''
    #initial conditions
    psi,phi = 0.0,1.0
    r = array([psi,phi],float)
    N = 1000
    h = abs(a-b)/N
    PSI = []

    #obtain the solution from runge-kutta and return end value
    for x in arange(a,b,h):
        PSI.append(psi)
        r += rk4(r,x,h,E)
        psi,phi = r
    return array(PSI)


def Solve(a,b,E):
    ##Same as above, only returns last value in the solution
    ##this makes it slightly quicker
    #initial conditions
    psi,phi = 0.0,1.0
    r = array([psi,phi],float)
    N = 1000
    h = abs(a-b)/N
    #obtain the solution from runge-kutta and return end value
    for x in arange(a,b,h):
        r += rk4(r,x,h,E)
    psi,phi = r
    return psi

def normalisation(PSI):
    '''Function uses simple Trapezoidal rule to find the
    normalisation constant of the wavefunction'''
    psi_sq = abs(PSI)**2
    integral = 0.5*(psi_sq[0]+psi_sq[-1]) + sum(psi_sq[1:-1])
    return sqrt(integral)
    

##Obtain solutions to the first three energy states of the quantum osc.
for i,E2 in enumerate([e,500*e,1000*e]):
    #initialise E1 and psi2 guess 
    E1 = 0.0
    psi2 = Solve(x0,xL,E1)
    while abs(E1 - E2) > target:
        psi1,psi2 = psi2,Solve(x0,xL,E2)
        E1,E2 = E2,E2 - psi2*(E2 - E1)/(psi2 - psi1)

    #E_n = (n + 1/2)hw
    print "E%d = "%(i),E2/e,"eV"

    figure(i)
    #calculate the wavefunction with the quantized energy
    PSI = wavefunction(-5*a,5*a,E2)
    #calculate the normalisation constant
    norm_const = normalisation(PSI)
    psi_norm = PSI/norm_const
    #area under the normalised wavefunction should equal 1
    print normalisation(psi_norm)
    plot(psi_norm)
    
show()


 
