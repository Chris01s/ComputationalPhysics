from numpy import*
from numpy.fft import rfft,irfft
from pylab import plot,show,figure

def dct(y):
    N = len(y)
    y2 = empty(2*N,float)
    for n in range(N):
        y2[n] = y[n]
        y2[2*N-1-n] = y[n]
    c = rfft(y2)
    phi = exp(-1j*pi*arange(N)/(2*(N)))
    return real(phi*c[:N])

dow2 = loadtxt("cpresources/dow2.txt",float)
N = len(dow2)
plot(dow2)

c = rfft(dow2)
c[int(0.02*N):] = 0
c = irfft(c)
plot(c)

c = dct(dow2)
c[int(0.02*N):] = 0
c = irfft(c)
plot(c[:N+1])
show()

