from numpy.random import random
import numpy as np

def f(x):
	return 1.0/(np.exp(x) + 1)

#p(x) = w(x)/int w(x) = 1/2sqrt(x)

N = 1000000
z = random(N)
#if w(x) = 1/sqrt(x), then by the transformation process we
#we end up with x=z^2
x = z**2
I = 2.0/N*sum(f(x))
print I


