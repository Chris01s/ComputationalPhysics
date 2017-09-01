from numpy import array,sqrt,pi

def func(x):
    return sqrt(1.0 - x**2)

def integral(func,N):
    integrate = 0.0
    h = 2.0/N
    for k in range(N):
        x = -1 + h*k
        integrate += h*func(x)
    return integrate

#a)
N = 100
print pi/2, integral(func,N)

#b)
Integrals = [integral(func,N) for N in range(1000,10000,1000)]
print Integrals
