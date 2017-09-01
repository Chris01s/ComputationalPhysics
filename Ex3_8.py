from numpy import array,loadtxt,transpose
from pylab import plot, figure, show

#a)
x,y = transpose(loadtxt('cpresources/millikan.txt',float))
plot(x,y,'.')

#b)
def LeastSq(x,y):
    N = len(x)
    Ex = sum(x)/N
    Ey = sum(y)/N
    Exx = sum(x**2)/N
    Exy = sum(x*y)/N

    m = (Exy - Ex*Ey)/(Exx - Ex**2)
    c = (Exx*Ey - Ex*Exy)/(Exx - Ex**2)
    return m,c

m,c = LeastSq(x,y)
print m,c

#c)
linFit = m*x + c
plot(x,y,'.',x,linFit,'-')
show()

#d)
h = 6.63E-34
e = h/m
print e, " which is ", (e-1.602E-19)/1.602E-19 * 100, " percent from the accepted"
print "value."
