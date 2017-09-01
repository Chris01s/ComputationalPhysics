import numpy as np
import cmath as cm
from pylab import plot, show, xlim

def DFT(y):
    N = len(y)
    c = 0
    k = np.arange(N)
    for n in range(N//2):
        c += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c

def DFT2D(y):
    M,N = np.shape(y)
    c = np.zeros((M,N//2+1),complex)
    for k in range(M):
        for l in range(N//2+1):
            for m in range(M):
                for n in range(N//2+1):
                    c[k,l] += y[m,n]*np.exp(-2j*np.pi*(k*m/M + l*n/N))
    return c

def dft2(y):
    M,N = np.shape(y)
    a = empty([M,N],complex)
    b = empty([M,N],complex)

    for i in range(M):
        a[i] = DFT(y[i])
    for j in range(N):
        b[:,j] = DFT(a[:,j])

    return b

def dct2(y):
    M,N = np.shape(y)
    a = empty([M,N],float)
    b = empty([M,N],float)

    for i in range(M):
        a[i,:] = dct(y[i,:])
    for j in range(N):
        b[:,j] = dct(a[:,j])

    return b

def dctI(y):
    N = len(y)
    c = zeros(N,float)
    for k in range(N):
        for n in range(1,N//2):
            c[k] += 2*y[n]*cos(-2*pi*k*n/N)
        c[k] += y[0] + y[N//2]*cos(-2*pi*k*(N//2)/N)
    return c

def dctII(y):
    N = len(y)
    c = zeros(N,float)
    for k in range(N):
        for n in range(N//2):
            c[k] += y[n]*cos(-2*pi*k*(n+1/2)/N)
        c[k] *= 2
    return c                    
