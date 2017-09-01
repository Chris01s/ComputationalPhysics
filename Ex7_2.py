from pylab import plot,show,xlim,ylim,figure,xlabel,ylabel
from numpy import loadtxt,zeros,exp,pi,arange,where

def dft(y):
    N = len(y)
    c = zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c

time, sunspots = loadtxt('ExamplesAndUseful\sunspots.txt',float).T
figure(1)
plot(time,sunspots)

#Fourier Transform the data
c = dft(sunspots)
power = abs(c[1:])**2 #exclude 1st point(sum of coefficients)
N = len(c)
figure(2)
k = arange(1,N)
freq = k/(2*float(N))
plot(freq,power)
period = 1/freq
cycle = max(power)
show()
