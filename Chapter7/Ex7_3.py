from numpy import loadtxt
from numpy.fft import rfft
from pylab import plot,show,figure

freq = arange(0,44100,1)

#piano
piano = loadtxt('ExamplesAndUseful\piano.txt',float)
cpiano = rfft(piano)
figure(1)
plot(piano)
figure(2)
plot(abs(cpiano[:10000]))

#trumpet
trumpet = loadtxt('ExamplesAndUseful/trumpet.txt')
ctrumpet = rfft(trumpet)
figure(3)
plot(trumpet)
figure(4)
plot(abs(ctrumpet[:10000])**2)
show()

