from numpy import arange
from numpy.fft import rfft,irfft
from pylab import plot,show,figure

def f(t):
    if int(2*t)%2 == 0:
        return 1
    else:
        return -1

#input
t = arange(0,1,0.001)
#build square wave
square = [f(i) for i in t]
#plot
plot(t,square)

#fast fourier transform of square wave
c = rfft(square)
#equal all but first 10 coefficients to zero
c[9:] = 0
#inverse fft to retreive square wave
c = irfft(c)
#plot
plot(t,c)
show()
#again, what we're seeing is the effect of eliminating higher
#frequencies in the harmonic series. This is the same effect
#that compression and reformating of audio and image files
#has on the quality of the files.
