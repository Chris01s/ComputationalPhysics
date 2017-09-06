from numpy import zeros, transpose,sqrt, identity,array,diag
import sys
sys.path.append('C:\Users\CHRIS\Documents\Python Scripts\LearningScripts\NumericalMethods')
from LU_Decomp import MatMult

##MatMult is a function I wrote for fun to calculate the dot product of
##two matrices. You can just replace this with np.dot function if you wish, but
##I thought it to be a healthy exercise to write my own dot product function
##with cost in calculation time

#a)
def QR_Decomp(A):
    '''calculates the QR decompostion of the matrix A'''

    def mag(u):
        '''returns magnitude of a vector, u'''
        return sqrt(sum(u**2))

    #intialise Q and U matrices
    N = len(A)
    Q = zeros((N,N),float)
    U = zeros((N,N),float)
    
    #populate Q and U     
    for i in range(N):
        U[:,i] = A[:,i]
        for j in range(i):
            U[:,i] -= sum(Q[:,j]*A[:,i])*Q[:,j]
        Q[:,i] = U[:,i]/mag(U[:,i])

    R = MatMult(transpose(Q),A)
    return Q,R

#b)
##test
A = array([[ 1.,  4.,  8.,  4.],
           [ 4.,  2.,  3.,  7.],
           [ 8.,  3.,  6.,  9.],
           [ 4.,  7.,  9.,  2.]])
Q,R = QR_Decomp(A)
#close enough

#c)

def EigenV(A):
    '''Performs QR algorithm on the symmetric (Hermitian) matrix, A
    to calculate its eigenvectors and eigenvalues:
        A is assumed to be symmetric of Hermitian'''
    #initial coditions
    N = len(A)
    V = identity(N,float)
    epsilon = 1E-10
    while True:
        flag = 0
        Q,R = QR_Decomp(A)
        A = MatMult(R,Q)
        V = MatMult(V,Q)
        for j in range(N):
            for k in range(N):
                if j == k:
                    continue
                else:
                    if abs(A[j,k]) < epsilon:
                        flag = 1
                        break
            if flag == 1:
                break
        if flag == 1:
            break
    return V,diag(A)

#test
eigvec, eigval = EigenV(A)
#surprisingly close!!
