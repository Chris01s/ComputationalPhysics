from numpy import linspace, tanh, cosh, array, arange, zeros
from pylab import plot, show, figure


##Forward difference: (f(x+h) - f(x))/h
def forward_diff(f,x,h):
    return (f(x+h) - f(x))/h


f = lambda x: 1 + 0.5*tanh(2*x)
x = linspace(-2,2,100)
h = 1E-3
fprime = forward_diff(f,x,h)
print fprime

##central difference: (f(x+h) - (f(x-h))/2h
def central_diff(f,x,h):
    return (f(x+h/2) - f(x-h/2))/(h)

fprime = central_diff(f,x,h)

figure(1)
plot(x,fprime,'.', x, 1 - tanh(2*x)**2)
show()

##higher order approximations of the first derivative:
def higher_approx(f, x, h, coeff, m):
    coeff = array(coeff)
    j = arange(-m,m+2,2)/2.0
    derivative = f(x + j*h)*coeff
    return sum(derivative)/h

coeffs =  [[-1, 1],\
          [-0.5, 0, 0.5], \
          [1/24.0,-27/24.0, 27/24.0, -1/24.0],\
          [1/12.0, -2/3.0, 0, 2/3.0, -1/12.0],\
          [-3/640.0, 25/384.0, -75/64.0, 75/64.0, -25/384.0, 3/640.0]]
figure(2)
m = 0
result = zeros(len(x))
for coeff in coeffs:
    m += 1
    for i,j in enumerate(x):
        result[i] = higher_approx(f,j,h,coeff,m)
    plot(x, result, '-', label = 'm = %d'%(m))
show()
    
##second derivative
def second_deriv(f,x,h):
    return (f(x+h) - 2*x + f(x-h))/h**2

##partial derivate
def partial_deriv(f,x,y,h,str(param)):
    if param == "x":
        return (f(x+h/2,y) - f(x-h/2,y))/h
    elif param == "y":
        return (f(x,y+h/2) - f(x,y-h/2))/h

def second_partial_deriv(f,x,y,h):
    a = f(x+h/2,y+h/2)
    b = f(x-h/2,y+h/2)
    c = f(x+h/2,y-h/2)
    d = f(x-h/2,y-h/2)
    return (a - b - c + d)/h**2




        
