from numpy import array


##perfroms Simpson Rule of integration
def Trap(f,a,b,N):
    h = abs(a-b)/N
    I = 0.5*(f(a) + f(b))
    for k in range(1,N):
        I += f(a + k*h)
    return h*I


##perfroms Simpson Rule of integration
def Simps(f,a,b,N):
    h = abs(a-b)/N
    Simp = 0 
    for k in range(1,N):
        if k%2 != 0:
            Simp += 4*f(a + k*h)
        else:
            Simp += 2*f(a + k*h)
    return (f(a) + f(b) + Simp)*h/3.0
#function
def f(x):
    return x**4 - 2*x + 1

a = 0.0
b = 2
print Simps(f,a,b,10)

#b)
print "Fractional Error: ",(Simps(f,0.0,2,10) - 4.4)/4.4 

#c)
Trapezoid = array([Trap(f,a,b,N) for N in (10,100,1000)])
Simpsons = array([Simps(f,a,b,N) for N in (10,100,1000)])
print "N: ",(10,100,1000), "\nTrapezoid: ",(Trapezoid - 4.4)/4.4, "\n", "Simpson's: ",(Simpsons - 4.4)/4.4


