import numpy as np
from pylab import plot, show,xlabel,ylabel
import sys

sys.path.append('C:\Users\CHRIS\Documents\Python Scripts\LearningScripts\ComputationalPhysicsExercises\cpresources')
import gaussxw as G

def f(x):
	return (x**3)/(np.exp(x) - 1)
	
def f_prime(z):
	return (1/(1-z)**2)*f(z/(1-z))

#a) and b)
N = 1000
a,b = 0,1
x,w = G.gaussxwab(N,a,b)
k = 8.31/6.022E23
c = 1/np.sqrt(4*np.pi*1E-7*8.85E-12)
hbar = 6.63E-34/(2*np.pi)
sig = k**4 * sum(f_prime(x)*w)/((2*np.pi*c)**2 * hbar**3)
print sig
#Output: 5.64184760521e-08

# T = np.arange(300.0,1000.0,10)
# plot(T**4,sig*T**4)
# show()


