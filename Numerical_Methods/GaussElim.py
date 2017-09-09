from numpy import shape, reshape, concatenate, transpose, copy, identity, prod, diagonal

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
    A_v = concatenate((A,v),axis = 1)

    #Perform Gaussian Elimination
    #First, check for row pivoting
    for i in range(N):
        if A_v[i,i] == 0:
            Temp = copy(A_v[i])
            A_v[i] = A_v[i+1]
            A_v[i+1] = Temp

        #perform Gauss Elmination
        A_v[i] /= A_v[i,i]
        for j in range(i+1,N):
            if A_v[j,i] == 0:
                continue
            else:
                A_v[j] -= A_v[i]*A_v[j,i]
                
    #Now for backsubstitution
    v = A_v[:,-1]
    v = v.reshape(N,1)

    for i in range(N-1,-1,-1):
        for j in range(i+1,N):
            v[i] -= A_v[i,j]*v[j]

    v = transpose(v)[0]
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

    return A_I[:,N:]


def MDet(A):
    '''Function to perform Gauss Elimination Method
       to set for the determinant of matrix A.
    '''

    N = len(A)

    #Perform Gaussian Elimination to build up U upper triangular matrix
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
        


