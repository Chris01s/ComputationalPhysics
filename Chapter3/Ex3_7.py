from numpy import *
from pylab import imshow,show

x,y = mgrid[-2:2:100j,-2:2:100j]
c = x + y*1j

def mandelbort(c,n=100):
    z = 0
    for i in range(n):
        z = c + z**2
    z_mod = sqrt(z * z.conjugate())
    return z_mod<2
	
imshow(mandelbort(c))
show()
