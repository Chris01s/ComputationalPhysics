#Ex 5.20
from numpy import linspace, sin
from pylab import plot, show

def sinc(x):
    if x == 0:
        return 1
    else:
        return (sin(x)/x)**2

def f(x):
    return x**4 - 2*x + 1

     
def Super_Adapt_Trap(f, a, b):
    '''
        Performs an Adaptive Trapezoidal Method by calculating an initial
    guess, doubling the number of steps, calculating another guess
    by using the previous guess and then the error between the two guesses.
    If this guess is less than a tolerance level (1e-10), the function
    returns the latter calculation result.
    args:
        f: function to be integrated
        a: lower limit
        b: upper limit
    '''
    #function to evaluate the integrals with 1 and 2 slices
    def step(x1,x2,f1,f2):
        '''
            args:
                x1: lower limit of integral
                x2: upper limit of integral
                f1: function evaluated at lower limit
                f2: ''      ''          '' upper limit
        '''
        #establish two different width sizes
        h1 = abs(x1-x2)
        h2 = h1/2.0
        #take mid-point between the two limits and evaluate the function at that point
        xmid = abs(x1+x2)/2.0
        fmid = f(xmid)
        #using these two widths, evaluate the integral using trapezoid rule
        I1 = (f1 + f2)*h1/2.0
        I2 = (f1 + f2 + 2*fmid)*h2/2.0
        
        if abs(I2 - I1)/3 <= h1*delta:
            return h2*(f1 + 4*fmid + f2)/3.0
        else:
            return step(x1, xmid, f1, fmid) + step(xmid, x2, fmid,f2)

    epsilon = 1e-10
    delta = epsilon/(b-a)
    fa, fb = f(a), f(b)
    return step(a,b,fa,fb)

print Super_Adapt_Trap(sinc,0.0,10)


    
