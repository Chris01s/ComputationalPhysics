from DiscreteFFTs import DFT
from pylab import plot,show,xlim,ylim,figure
from numpy import pi,arange,sin,array,ones

def FFT(N,y,i):
    c = DFT(y)
    figure(i)
    plot(abs(c))

#Square wave    
N = 1000
y = ones(N)
y[N//2:N] = 0
FFT(N,y,1)

#Sawtooth
y = arange(0,N,1)
FFT(N,y,2)

#modulated sine wave
n = arange(0,N,1)
y = sin(pi*n/N)*sin(20*pi*n/N)
FFT(N,y,3)
show()

