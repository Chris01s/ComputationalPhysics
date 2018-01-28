from numpy.random import standard_normal
from random import random
import numpy as np
from pylab import plot,ylabel,show,figure,legend

def f(x):
	return x**2 - np.cos(4*np.pi*x)

def g(x):
	return np.cos(x) + np.cos(np.sqrt(2)*x) + np.cos(np.sqrt(3)*x)
	


if __name__=="__main__":
	Tmax = 1.0
	Tmin = 1E-5
	tau = 1E4
	
	x = 2.0
	xplot = [x]
	soln = f(x)
	
	t = 0
	T = Tmax
	while T>Tmin:
		t += 1
		T = Tmax*np.exp(-t/tau)
		
		old_soln = soln
		dx = standard_normal()
		x += dx
			
		soln = f(x)
		delta = soln - old_soln
		
		if random()>np.exp(-delta/T) or x > 50 or x < 0:
			x -= dx
			soln = old_soln
			
		xplot.append(x)

figure(2)
plot(xplot,'.')
show()
			
		
		
		
		
		
