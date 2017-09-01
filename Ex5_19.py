from numpy import linspace, pi, sqrt, sin, exp,real,imag
from pylab import figure, imshow, plot, show,gray

#a) seperation is d, but to obtain this in radians we take pi/d
#b)
d = 20E-6
alpha = pi/d
#transmission function
def q(u):
    return sin(alpha*u)**2

#c)
wavelength = 500E-9
focal_length = 1
k = 2*pi/wavelength
width = 10*d
#function to be integrated
def Integrand(f,u,x):
    return sqrt(f(u))*exp(1j*k*x*u/focal_length)

#integration 
def I(f,x):
    a = -width/2
    b = width/2
 
    ##perfroms Trapezoidal Rule of integration
    N = 100
    h = abs(a-b)/N
    result = Integrand(f,a,x) + Integrand(f,b,x)
    for k in range(1,N):
        result += Integrand(f,a + k*h,x)

    return (h*(real(result) + imag(result)))**2


figure(1)
x = linspace(-0.05,0.05,300)
intensity = I(q,x)
plot(x,intensity,'-')
show()

#d)
figure(2)
gray()
imshow([intensity],aspect=100, vmax=0.25*max(intensity))


#e)i)
def t(u):
    return (sin(alpha*u)*sin(u*alpha/2))**2

intensity = I(t,x)
figure(3)
plot(x,intensity,'-')
show()

figure(4)
gray()
imshow([intensity],aspect=100, vmax=0.25*max(intensity))

#e)ii)

d = 60E-6
alpha = pi/d
width = 10E-6

intensity1 = I(q,x)
figure(5)
plot(x,intensity1,'-')
show()

figure(6)
gray()
imshow([intensity],aspect=100, vmax=0.25*max(intensity))








