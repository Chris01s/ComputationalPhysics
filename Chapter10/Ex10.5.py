from math import sin,sqrt
from random import random

def f(x):
	return (sin(1/(x*(2-x))))**2
	
def FullMonte(N,A,f):
	count = 0
	for i in range(N):
		x = A*random()
		y = random()
		if y<f(x):
			count+=1
	return A*count/N

def meanValue(N,a,b,f):
	I = 0.0
	sqavg = 0.0
	for i in range(N):
		x = random()
		I += f(x)
		sqavg += f(x)**2
	sqavg /= N
	avg = I/N
	var = sqavg - avg**2
	std = abs(b-a)*sqrt(var/N)
	I *= abs(b-a)/N
	return I, std

N = 10000
A = 2.0
I = FullMonte(N,A,f)
print I, sqrt(I*(2.0-I)/N)

a = 0.0
b = 2.0
I,std = meanValue(N,a,b,f)
print I,std






