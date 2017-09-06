from numpy import array
#a)
def f(x):
    return x*(x-1)

def deriv(x,delta):
    return (f(x+delta) - f(x))/delta

x = 1
delta = 1e-2
print f(x), deriv(x,delta), delta

print "analytical is: ", x - 1 + x
#the value for delta is too big

#b)
delta = array([10.0**(-a) for a in range(4,16,2)],float)
print deriv(x,delta) #accuracy gets better then worse 


