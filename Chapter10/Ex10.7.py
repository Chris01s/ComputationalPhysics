from numpy.random import random
import numpy as np

def f(r):
	return np.sum(r**2,axis=1)<=1
	
def g(r):
	if sum(r**2)<=1:
		return 1
	else:
		return 0

def montecarlo(N,dim,a,b):
	I = 0
	for i in range(N):
		r = (b-a)*random(dim) + a
		I += g(r)
	return ((b-a)**dim)/N*I

def monteCarlo_quicker(N,dim,a,b):
	r = (b-a)*random((N,dim)) + a
	fr = f(r)
	I = sum(fr)*(b-a)**dim/N
	return I



N = 1000000
dim = 10
a, b = -1.0, 1.0
I = monteCarlo_quicker(N,dim,a,b)
print I
