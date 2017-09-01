from cmath import exp
from numpy import pi,real, array

def f(z):
    return exp(2*z)

def factorial(n):
    if n<=0:
        return 1
    else:
        return n*factorial(n-1)

N = 10000
for m in range(21):
    fmprime = 0
    for k in range(N):
        fmprime += f(exp(1j*2*pi*k/N))*exp(-1j*2*pi*k*m/N)
    print abs(fmprime)*factorial(m)/N
