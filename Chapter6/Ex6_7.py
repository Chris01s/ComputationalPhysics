from numpy import zeros, array
import sys
sys.path.append('C:\Users\CHRIS\Documents\Python Scripts\LearningScripts\NeumannExercises')
from banded import banded


#b)
V = 5 #voltage
N = 6
#set up banded matrix
A = zeros([5,N],float)
A[0,:] = -1
A[1,:] = -1
A[2,:] = 4
A[3,:] = -1
A[4,:] = -1
A[0,0] = 3
A[-1,-1] = 3

w = zeros(N,float)
w[0] = V
w[1] = V

v = banded(A,w,2,2)

print v

#c)
V = 5 #voltage
N= 1000
#set up banded matrix
A = zeros([5,N],float)
A[0,:] = -1
A[1,:] = -1
A[2,:] = 4
A[3,:] = -1
A[4,:] = -1
A[0,0] = 3
A[-1,-1] = 3

w = zeros(N,float)
w[0] = V
w[1] = V

v = banded(A,w,2,2)

print v



