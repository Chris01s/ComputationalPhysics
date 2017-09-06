from numpy import array,ndarray,sin,sqrt,zeros

#a)
def Trap(func, a, b, N):
    h = abs(a - b)/N
    Trap = 0.5*(func(a) + func(b))
    for k in range(1,N):
        Trap += func(a + k*h)
    return h*Trap

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
    eps = 1E-6
    I = ndarray(2)
    I[0] = Trap(func, a, b, N)
    I[1] = 0
    
    while abs(I[1] - I[0])/3.0 > eps:
        N *= 2
        h = abs(a - b)/N

        for k in range(1,N,2):
            I[1] += h*func(a + k*h)

        I[1] += I[0]*0.5

        if abs(I[1] - I[0])/3.0 < eps:
            print N, ":", I[1], int(N/2.0)," : ", I[0]
            break
        else:
            print N, ":", I[1], " ",int(N/2.0),":", I[0], "err: ", abs(I[1] - I[0])/3.0
            I[0] = I[1]
            I[1] = 0
        
    return I[1]

def g(x):
    return sin(sqrt(100.0 *x))*sin(sqrt(100.0*x))

a,b,N = 0.0,1.0, 1
Adapt_Trap(g,a,b,N)

#Output:
##2 : 0.325231907806 0  :  0.147979484547
##4 : 0.512282850723 2  :  0.325231907806
##8 : 0.402997448478 6  :  0.512282850723
##16 : 0.430103369295 14  :  0.402997448478
##32 : 0.448414665787 30  :  0.430103369295
##64 : 0.453912931215 62  :  0.448414665787
##128 : 0.455348504373 126  :  0.453912931215
##256 : 0.455711266453 254  :  0.455348504373
##512 : 0.455802199652 510  :  0.455711266453
##1024 : 0.455824948132 1022  :  0.455802199652
##2048 : 0.455830636202 2046  :  0.455824948132
##4096 : 0.455832058278 4094  :  0.455830636202




#b)

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

print "\n"
I = Romberg_Trap(g,a,b,4)


