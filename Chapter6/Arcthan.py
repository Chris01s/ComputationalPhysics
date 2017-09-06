from numpy import tanh,cosh,linspace
from pylab import plot,show


def arctanh(u,acc):
    x = 0.0
    while True:
        delta = (tanh(x)-u)*cosh(x)*cosh(x)
        x -= delta
        if abs(delta)< acc:
            break
    return x
acc = 1E-15
U = linspace(-1,1,100)
atanh = [arctanh(u,acc) for u in U]
plot(U,atanh)
show()
