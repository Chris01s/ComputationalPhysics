import numpy as np
from pylab import plot, show
import sys

sys.path.append('C:\Users\CHRIS\Documents\Python Scripts\LearningScripts\ComputationalPhysicsExercises\cpresources')
import gaussxw as G



def f(x):
    return np.exp(x)*(x**4)/(np.exp(x) - 1)**2

def cv(T,x,w):
    xp = 0.5*T*x + 0.5*T
    wp = 0.5*T*w
    #calculate integral
    CV = sum(f(xp)*wp)
    return CV

N = 50
x,w = G.gaussxw(N)

#define constants
V = 1E-3
rho = 6.022E28
theta = 428
Boltz = 1.38E-23
T = np.linspace(5,500,100)
kappa = 9*V*rho*Boltz*(T/theta)**3


Heat_Cap = np.array([cv(theta/Tn,x,w) for Tn in T])*kappa
plot(T,Heat_Cap)
show()
