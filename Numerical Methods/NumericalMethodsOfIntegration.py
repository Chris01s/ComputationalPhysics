from numpy import arange, exp, ndarray, zeros, sqrt, sin
import sys

sys.path.append('C:\Users\CHRIS\Documents\Python Scripts\LearningScripts\ComputationalPhysicsExercises\ExamplesAndUseful')
import gaussxw

def f(x):
    return x**4 - 2*x + 1

def g(x):
    return sin(sqrt(100.0 *x))*sin(sqrt(100.0*x))

def E(t):
    return exp(-t**2)

def sinc(x):
    if x == 0:
        return 1
    else:
        return (sin(x)/x)**2

def Trap(func, a, b, N):
    h = abs(a - b)/N
    Trap = 0.5*(func(a) + func(b))
    for k in range(1,N):
        Trap += func(a + k*h)
    return h*Trap

def Simps(func, a, b, N):
    Simp = func(a) + func(b) 
    h = abs(a - b)/N
    for k in range(1, N):
        if k%2 != 0:
            Simp += 4*func(a + k*h)
        else:
            Simp += 2*func(a + k*h)
    return Simp*h/3


def Adapt_Trap(func, a, b, N):
    '''Performs an Adaptive Trapezoidal Method by calculating an initial
    guess, doubling the number of steps, calculating another guess
    by using the previous guess and then the error between the two guesses.
    If this guess is less than a tolerance level (1e-10), the function returns
    the latter calculation result.
    args:
        func: Function to be integrated
        a: lower limit of the integral
        b: upper limit of the integral
        N: number of trapezoid slices to evaluate the integral. 
    '''
    eps = 1E-10
    I = ndarray(2)
    I[0] = Trapettoni(func, a, b, N)
    I[1] = 0
    
    while abs(I[1] - I[0])/3.0 > eps:
        N *= 2
        h = abs(a - b)/N

        for k in range(1,N,2):
            I[1] += h*func(a + k*h)

        I[1] += I[0]*0.5

        if abs(I[1] - I[0])/3.0 < eps:
            print I[1]
            break
        else:
            I[0] = I[1]
            I[1] = 0
        
    return I[1]


def Adaptive_Simp(f,a,b):
    N = 1
    epsilon = 1E-6
    h = abs(b-a)/N
    
    S1 = (f(a) + f(b) + 2*sum([f(a + k*h) for k in range(2,N-1,2)]))/3.0
    T1 = 2.0*sum([f(a + k*h) for k in range(1,N-1,2)])/3
    
    I1 = h*(S1 + 2*T1)
    I2 = 0.0

    while abs(I2 - I1)/15 > epsilon:
        N *= 2
        h = abs(b-a)/N
        T2 = 2.0*sum([f(a + k*h) for k in range(1,N,2)])/3
        S2 = S1 + T1
        I2 = h*(S2 + 2*T2)
        if abs(I2 - I1)/15 < epsilon:
            break
        else:
            I1, I2 = I2, 0.0
            S1, S2 = S2, 0.0
            T1, T2 = T2, 0.0
            print I1, N

    return I2, N


def Romberg_Trap(func, a, b, N):
    '''Performs the Romberg integration (adaptive) based on the trapezoidal
    method. Will hopefully get round to optimizing for Simpson's Rule and
    Adaptive Trapezoidal method for quicker covergence.
    args: func, a, b, N.
    
        func: This requires the input of a predefined function in the existing
        workspace or script.
        a: lower limit of the integrand (type float)
        b: upper limits of the integrand (type float)
        N: An integer value to specify the size of the square matrix
        where the results of the integration will be stored.
        
    The romberg integration method establishes a column vector of initial
    calculations of the integral -- through Trapezoid, Simpson's Rule, or
    some other known method. Each successive calculation within this column ve
    -ctor is performed by consecutively doubling the number of Trapezoids,
    or number of steps, each time. e.g. N = 4 (within an analytical solution
    of, say, "5.00000.."): 
    
    1   4.945678----
                   |
    2   5.167890---  ->  New Guess 1--- 
                   |                 |
    3   5.128877---  ->  New Guess 2---... New guess 1
                   |                 |
    4   4.9882793--  ->  New Guess 3---... New guess 2.....SOLUTION!

    Once the specified number of intial calculations, N, have been performed,
    new guesses are then calculated from the existing pool of initial guess
    -- this means no further integration calculations are required, and the
    numerical solution converges much quicker than Trapezoid method alone.
    Each "new guess" calculation is performed by using the difference between
    adjacent values in each column and the order of uncertainty in the
    calculation:
         I_j,i = I_j-1,i+1 + (I_j-1,i+1 - I_j-1,i)/(4**n - 1)
         ex/
             New Guess1 = 5.167890 + (5.167890 - 4.945678)/(4 - 1)

    where i is the number element index, and j the column index of the NxN
    Romberg matrix, and n is the order of uncertainty ("_" denotes subscript).
    '''
    
    #intialize empty array of size NxN and stepsize
    R = zeros((N,N))
    steps = 1
    #calculate the first column vector: the initial guesses of the integral
    #each time doubling the number of Trapezoids
    for i in range(len(R[0])):
        R[i,0] = Trap(func, a, b, steps)
        steps *= 2
##    #using the above calculations (the initial guesses) perform the Romberg
##    #calculations (new guesses)
    for m in range(1,len(R)):
        for l in range(m,len(R)):
            R[l,m] = R[l,m-1] - (R[l,m-1] - R[l-1,m-1])/(4**m - 1)
    return R

def GaussLeGde(func, a, b, N):
    x, w = gaussxw.gaussxw(N)
    x = 0.5*((b-a)*x + (b+a))
    w = 0.5*w*(b-a)
    integral = 0.0
    for i in range(N):
        integral += w[i]*func(x[i])
    return integral

def DoubleInt(func, a, b, N):
    '''first argument must be a function
        that relies on at least 2 different variables'''
    x, w = gaussxw.gaussxw(N)
    x = 0.5*((b-a)*x + (b+a))
    w = 0.5*w*(b-a)
    y = x
    integral = 0
    for i in range(N):
        for j in range(N):
            integral += w[i]*w[j]*func(x[i],y[j], z = 0)
    return integral

##Test!!
##print Trapettoni(f,0.,2.,1000000)
##print TheSimpsons(f,0.,2.,10)
##print Adapt_Trap(f,0.,2.,2)
##print GaussLeGde(f,0.,2.,3)
##print Romberg_Trap(f,0.,2.,5)
##x = arange(0, 3.0, 0.1)
##result = 0
##for i in range(1,len(x)):
##    h = abs(x[i-1] - x[i])/N
##    result += TheSimpsons(E, x[i-1], x[i], h, N)
##    print result




