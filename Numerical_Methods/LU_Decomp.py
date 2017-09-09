from numpy import zeros, shape, reshape, concatenate, array,where
from numpy import transpose, copy, identity, prod, diagonal

def GaussElim(A,v):
    '''Function to perform Gauss-Jordan Elimination Method
       to set of solve linear equations.
       args:
       A: Array of equation coefficients (must be a square matrix)
       v: vector array of resulting values for each equation
    '''
	
    #Set up the matrix in row echelon form
    N = len(A)
    v = v.reshape(N,1)
    Av = concatenate((A,v),axis = 1)

    #Perform Gaussian Elimination
    #First, check for row pivoting
    #initialise scale factor vector
    sFactor = array([max(abs(A[i])) for i in range(N)], float)
    
    for i in range(N-1):
        #calculate which row to pivot
        r = zeros(N)
        for j in range(i,N):
            r[j:] = abs(Av[j,i])/sFactor[j]
            
        #Do pivot 
        pivot = where(abs(r) == max(abs(r)))[0][0]
        Alist = list(Av)
        sFactorList = list(sFactor)
        Alist[i], Alist[pivot] = Alist[pivot], Alist[i]
        sFactorList[i], sFactorList[pivot] = sFactorList[pivot], sFactorList[i]
        Av = array(Alist)
        sFactor = array(sFactorList)

        #perform Elmination sub-procedure
        for j in range(i+1,N):
            if Av[j,i] == 0:
                continue
            else:
                Av[j] -= Av[i]*Av[j,i]/Av[i,i]
                
    #Now for backsubstitution
    v = Av[:,-1]
    for i in range(N):
        Av[i] /= Av[i,i]
    for i in range(N-1,-1,-1):
        for j in range(i+1,N):
            v[i] -= Av[i,j]*v[j]

    return v




def Minv(A):
    '''Function to perform Gauss-Jordan Elimination Method
       to set of solve linear equations.
       args:
       A: Array of equation coefficients (must be a square matrix)
       v: vector array of resulting values for each equation
    '''
	
    #Set up the matrix in row echelon form
    N = len(A)
    I = identity(N)
    A_I = concatenate((A,I),axis = 1)

    #Perform Gaussian Elimination
    #First, check for row pivoting
    for i in range(N):
        if A_I[i,i] == 0:
            Temp = copy(A_I[i])
            A_I[i] = A_I[i+1]
            A_I[i+1] = Temp

        #perform Gauss Elmination
        A_I[i] /= A_I[i,i]
        for j in range(i+1,N):
            if A_I[j,i] == 0:
                continue
            else:
                A_I[j] -= A_I[i]*A_I[j,i]

    #First, check for row pivoting
    for i in range(N-1,0,-1):
        #Now for reverse elimination
        for j in range(i-1,-1,-1):
            A_I[j] -= A_I[i]*A_I[j,i]

    return A_I




def MDet(A):
    '''Function to perform Gauss Elimination Method
       to set for the determinant of matrix A.
    '''
    if shape(A)[0] != shape(A)[1]:
        return TypeError
    #Perform Gaussian Elimination to build up U upper triangular matrix
    N = len(A)
    SWAP = 1
    for i in range(N):
        if A[i,i] == 0:
            Temp = copy(A[i])
            A[i] = A[i+1]
            A[i+1] = Temp
            SWAP *= -1 #record if a swap was made, as this will affect the sign of the det

        #perform Gauss Elmination
        for j in range(i+1,N):
            if A[j,i] == 0:
                continue
            else:
                A[j] -= A[j,i]*A[i]/A[i,i]

    #Once U is obtained, perform product of diagonals and the flag
    determinant = prod(diagonal(A)) * SWAP
    
    return determinant




def MatMult(A,B):
    '''Performs Matrix Multiplication on two matrices, A and B '''
    rowsA, colsA = shape(A)
    rowsB, colsB = shape(B)
    C = zeros((rowsA,colsB),float)

    if colsA != rowsB:
        print "no. of cols of first matrix MUST equal no. of rows in second matrix"
        return TypeError
    else:
        if rowsA > 1 and colsB > 1:
            for i in range(rowsA):
                for j in range(colsB):
                    C[j,i] = sum(A[j]*B[:,i])

        elif colsB == 1 and rowsA == 1:
            C = sum(A*B[:,0])

        elif colsB == 1:
            for i in range(rowsA):
                C[i] = sum(A[i]*B[:,0])

        elif rowsA == 1:
            for i in range(rowsB):
                C[0][i] = sum(A[0]*B[:,i])
        return C



def MatMultMult(L):
    '''Performs matrix multiplication on a list of matrices.
     args:
         L = list/vector of matrices in the correct order in which they are to
         be multiplied e.g.:
             L = [L1,L2,L3] function will then return L1*L2*L3 matrix
    '''
    N = len(L)
    M1 = L[0]
    M1, M2 = L[0:2]
    Mn = MatMult(M1,M2)
    for n in range(2,N):
        Mn = MatMult(Mn,L[n])
    return Mn
          
     

def LUdecomp_Crout(A):
    '''Performs LU decomposition of the matrix A and returns the
        upper triangular, U, where L1L2L3...Ln*A = U. The function also returns
        the lower triangular L'''

    #Obtain size of matrix
    N = len(A)
    L = zeros((N,N),float)
    U = copy(A)
    for i in range(N):
        L[i:,i:][:,0] = U[i:,i:][:,0]
        B = identity(N,float)*U[i,i]
        B[i,i] /= U[i,i]
        B[i+1:,i] = U[i+1:,i]*(-1)
        B /= U[i,i]
        U = MatMult(B,U)

    return L,U


def LUdecomp_Dolittle(A):
    '''Performs LU decomposition of the matrix A and returns the
        upper triangular, U, where L1L2L3...Ln*A = U. The function also returns
        the lower triangular L'''

    #Perform Gaussian Elimination
    #First, check for row pivoting
    N = len(A)
    U = copy(A)
    L = identity(N,float)
    for i in range(N):
        if U[i,i] == 0.0:
            try:
                Temp = copy(U[i])
                U[i] = U[i+1]
                U[i+1] = Temp
            except:
                print TypeError

        #perform Gauss Elmination
        for j in range(i+1,N):
            if U[j,i] == 0:
                continue
            else:
                mult = U[j,i]/U[i,i]
                U[j] -= U[i]*mult
                L[j,i] = mult
    LU = copy(U)
    for i in range(1,N):
        LU[i,:i]=L[i,:i]
    return LU

def LUSolve(L, U, b):
    #Solve the equation Ly = b by forward substitute
    N = len(L)
    for i in range(1,N):
        b[i] -= sum(L[i,:i]*b[:i])

    #Solve the equation Ux = y
    b[-1] /= U[-1,-1]
    for i in range(N-2,-1,-1):
        for j in range(i+1,N):
            b[i] = (b[i] - U[i,j]*b[j])/U[i,i]
            
    return b
    
 
def QR_Decomp(A):
    '''calculation to retrieve the QR decomposition of the matrix, A'''

    def mag(u):
        '''finds the magnitude of a vector, u'''
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
		
	
			
