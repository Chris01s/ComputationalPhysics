import numpy as np
from pylab import plot, show,xlabel,ylabel
import sys

sys.path.append('C:\Users\CHRIS\Documents\Python Scripts\LearningScripts\ComputationalPhysicsExercises\cpresources')
import gaussxw as G


def I_I0(x,z,t,w):

    def u(x,z):
        lamda = 1
        return x*np.sqrt(2/(lamda*z))

    def C(t,w):
        return np.sum(np.cos(0.5*np.pi*t**2)*w,axis=1)

    def S(t,w):
        return np.sum(np.sin(0.5*np.pi*t**2)*w,axis=1)

    U = u(x,z)
    tp = 0.5*U*(t + 1)
    wp = 0.5*U*w

    print C(tp,wp),S(tp,wp)
    
    I = (2*C(tp,wp) + 1)**2 + (2*S(tp,wp) + 1)**2
    return I
   
N = 50
t,w = G.gaussxw(N)
t = t.reshape(1,N)
w = t.reshape(1,N)
X = np.arange(-5,5,0.1)
X = X.reshape(100,1)
z = 3.0
I = I_I0(X,z,t,w)/8.0
plot(X,I)
show()


