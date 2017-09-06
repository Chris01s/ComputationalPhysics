from numpy import pi,exp,arange,sqrt,sin,linspace,array
from numpy.fft import fft
from pylab import plot,show,imshow,figure


def I(x):

    def q(u):
        alpha = pi/20E-6
        return sin(alpha*u)**2

    N = len(x)
    n = arange(N)
    u = n*W/N - W/2
    y = sqrt(q(u))
    y[abs(u)>w/10] = 0.0

    #perform the dft equation stated in the question
    #can compare this to fft
    c = 0.0
    for n in range(N):
        c += y[n]*exp(-2j*pi*k*n/N)
    intensity = W*abs(c)/N
    return abs(intensity)**2

#set up conditions
lamda = 500E-9
f = 1
w = 200E-6
W = 10*w
k = linspace(-200,200,1000)
#calculations
x = f*lamda/W*k
intensity = I(x)
#plots
figure(1)
plot(x,intensity)
figure(2)
imshow([intensity],aspect='auto')
show()
