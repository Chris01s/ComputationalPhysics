from numpy import loadtxt,copy
from numpy.fft import rfft,irfft
from pylab import plot,show,figure

#Dow plot
dow = loadtxt('ExamplesAndUseful\dow.txt',float)
N = len(dow)

figure(1)
plot(dow)

c = rfft(dow)
c10perc = c.copy()
c10perc[int(0.1*N):] = 0
c10perc = irfft(c10perc)
plot(c10perc)
#what is happening is that the data is being smoothed, almost in the same way
#as what a running average does. However, how it is being acheived here is
#by cancelling out the higher frequencies from the data.

c2perc = c.copy()
c2perc[int(0.02*N):] = 0
c2perc = irfft(c2perc)
plot(c2perc)
show()
#Again, by cancelling out even more of the higher frequencies from the data
#we are left with one or two slight high frequencies and the fundamental freq
#-uency. This gives the effect of smoothing the data even more so.
#Remember, that the Fourier coefficients represent the amplitude of each freq
#-ency present in the signal, some are usually more prominent than others.
#But by zeroing all but the first 10 or 2 percent, we are cancelling these
#out. Then when we perform the inverse fft, we get back the signal with
#reduced higher frequencies.
