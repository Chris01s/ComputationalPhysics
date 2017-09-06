#Ex. 5.18

def func(x):
    return x**4 - 2*x + 1

def central_diff(f,x,h):
        return (f(x+h/2) - f(x-h/2))/(h)


def Euler_Maclaurin_Rule(function,a,b,N):
    h = abs(a - b)/N
    Integral = 0
    for k in range(1,N):
        Integral += function(a + k*h)*h
    Integral += h*(0.5*(function(a) + function(b)) \
                   + h*(central_diff(function,a,h) - \
                        central_diff(function,b,h))/12.0)
    return Integral

a = 0.0
b = 2.0
N = 10
result = Euler_Maclaurin_Rule(func,a,b,N)
print abs(result  - 4.4)

