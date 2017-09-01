from numpy import zeros
from pylab import plot,show
import sys
sys.path.append('C:\Users\CHRIS\Documents\Python Scripts\LearningScripts\MITFingerExercises')
import GaussElim

#Functions
def Tridiag(A,v):
    N = len(A)
    #Perform Gauss Elimination
    for i in range(N-1):
        A[i,i+1] /= A[i,i]
        v[i] /= A[i,i]
        A[i+1,i+1] -= A[i+1,i]*A[i,i+1]
        v[i+1]-= A[i+1,i]*v[i]

    v[N-1] /= A[N-1,N-1]

    #Back substitution
    x = zeros(N,float)
    x[N-1] = v[N-1]
    for i in range(N-2,-1,-1):
        x[i] = v[i] - A[i,i+1]*x[i+1]
        
    return x


def LinearMolecule(N,C,m,k,omega,alpha):
    #Set up the initial triadiagonal matrix
    A = zeros([N,N],float)
    for i in range(N-1):
        A[i,i] = alpha
        A[i,i+1] = -k
        A[i+1,i] = -k

    A[0,0] = alpha - k
    A[N-1,N-1] = alpha - k
    v = zeros(N,float)
    v[0] = C
    
    return A, v

def main():
    #Constants
    N = 26
    C = 1.0
    m = 1.0
    k = 6.0
    omega = 2.0
    alpha = 2*k - m*omega**2
    A, v = LinearMolecule(N,C,m,k,omega,alpha)
    x = Tridiag(A,v)
    plot(x)
    show()

if __name__ == "__main__":
    main()
