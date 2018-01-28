from numpy.random import random as randy
from numpy import log,sort
from pylab import plot,show

tau = 3.053*60
N = 100
mu = log(2)/tau
z = randy(N)
x = -log(1-z)/mu
x = sort(x)
survived = N - x
plot(survived)
show()
