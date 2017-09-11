from numpy import*
from pylab import plot,show,figure

def FFT(x):
    N = len(x)
    if N <= 1: return x
    E = FFT(x[0::2])
    O = FFT(x[1::2])
    T = [exp(-2j*pi*k/N)*O[k] for k in range(N//2)]
    return [E[k] + T[k] for k in range(N//2)] + \
           [E[k] - T[k] for k in range(N//2)]


y = loadtxt('cpresources/pitch.txt')
c = array(FFT(list(y)))
N = len(y)
plot(abs(c[:N//2]))
show()
