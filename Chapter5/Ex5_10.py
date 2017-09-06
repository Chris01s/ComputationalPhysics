import numpy as np
from pylab import plot, show,xlabel,ylabel
import sys

sys.path.append('C:\Users\CHRIS\Documents\Python Scripts\LearningScripts\ComputationalPhysicsExercises\cpresources')
import gaussxw as G


def V(x):
    return x**4

def Period(V,a,x,w):
    xp = 0.5*a*(x + 1)
    wp = 0.5*a*w
    
    E = V(a)
    f = 1/np.sqrt(E - V(xp))   
    T = np.sum(f*wp) 
    return T

N = 100
x,w = G.gaussxw(N)
m = 1.0
A = np.linspace(0,2,100,endpoint=True)
T = np.array([Period(V,a,x,w) for a in A],float) *np.sqrt(8*m)

plot(A,T)
xlabel('Amplitude')
ylabel('Period')
show()



## ###########################Vectorised method###########################
##import numpy as np
##from pylab import plot, show,xlabel,ylabel
##import sys
##
##sys.path.append('C:\Users\CHRIS\Documents\Python Scripts\LearningScripts\ComputationalPhysicsExercises\ExamplesAndUseful')
##import gaussxw as G
##
##
##def V(x):
##    return x**4
##
##def Period(V,a):
##    
##    N = 100
##    x,w = G.gaussxw(N)
##    xp = 0.5*a*(x + 1)
##    wp = 0.5*a*w
##    x = x.reshape(1,N)
##    w = w.reshape(1,N)
##    E = V(a)
##    f = 1/np.sqrt(E - V(xp))   
##    T = np.sum(f*wp,axis=1) 
##    return T
##
##m = 1.0
##A = np.linspace(0,2,100,endpoint=True)
##A = A.reshape(100,1)
##T = Period(V,A)*np.sqrt(8*m)
##plot(A,T)
##xlabel('Amplitude')
##ylabel('Period')
##show()
