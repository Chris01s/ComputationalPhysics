from numpy import sqrt, linspace, zeros, array,reshape
import sys
sys.path.append("C:\Users\CHRIS\Documents\Python Scripts\LearningScripts\ComputationalPhysicsExercises\cpresources")
from gaussxw import gaussxw
from pylab import plot, show

G = 6.674e-11
m = 1
ro = 100
N = 100
x,w = gaussxw(N)

def force(z):
    f = lambda x,y,z: (x**2 + y**2 + z**2)**(-3/2)
    a = -5
    b = 5
    xp = 0.5*(b-a)*x + 0.5*(b+a)
    yp = xp
    
    wp = 0.5*(b-a)*w
    
    s=0
    for i in range(N):
        for j in range(N):
            s+=wp[i]*wp[j]*f(xp[i],yp[j],z)
            
    return G * m * ro * z * s

z = linspace(0,10,50)
z.reshape(1,50)
F = force(z)
plot(z,F)
show()
