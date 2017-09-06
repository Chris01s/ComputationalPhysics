from numpy import pi, cos, sin, linspace, mgrid, sqrt
from pylab import plot, legend, show, imshow, figure, gray

def J(m,x):
    ''' Computes Bessel function. args: order(type:int),
        input value for the bessel function(type: float or 1darray)
        Return Value: function that produces results of Bessel function'''

    #function to be integrated
    def func(theta):
        return cos(m*theta - x*sin(theta))

    ##perfroms Simpson Rule of integration
    def Simps(f):
        N = 1000
        a = 0
        b = pi
        h = abs(a-b)/N
        Simp = 0 
        for k in range(1,N):
            if k%2 != 0:
                Simp += 4*f(a + k*h)
            else:
                Simp += 2*f(a + k*h)
        return (f(a) + f(b) + Simp)*h/3.0
    return Simps(func)

#a)
x = linspace(0,20,100)
figure(1)
for m in range(3):
    Bessel = J(m,x)/(pi)
    plot(x,Bessel,'-',label="m=%d"%(m))
legend(loc='UpperRight')
show()

###b)
###create a mesh-grid, two-dimensional grid space, to map the Bessel functions onto
##x,y = mgrid[-1:1:100j,-1:1:100j]
##lamda = 0.5 #wavelength of light in nm
##k = 2*pi/lamda #wave number
##r = sqrt(x**2 + y**2) #vector r
##I = (J(1,k*r)/(k*r))**2 #intensity function mapped onto the mesh-grid
##
##figure(2)
##imshow(I,cmap = "hot")
##
##figure(3)
##gray()
##imshow(I,vmax=0.1)
##







        
    
    
