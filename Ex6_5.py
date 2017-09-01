#Ex6.5
from numpy.linalg import solve
from numpy import array

#b)
##initialise values
R1 = R3 = R5 = 1E3
R2 = R4 = R6 = 2E3
C1 = 1E-6
C2 = 0.5E-6
x = 3
omega = 1/1E3

##set up array elements
a1, a2, a3 = 1/R1 + 1/R2 + 1j*omega*C1, - 1j*omega*C1, 0.0
a4, a5, a6 = -1j*C1*omega, 1/R2 + 1/R5 + 1j*omega*C1 + 1j*omega*C2, -1j*omega*C2
a7, a8, a9 = 0.0, -1j*omega*C2, 1/R3 + 1/R6 + 1j*omega*C2

##populate array (dtype as complex)
row1 = [a1, a2, a3]
row2 = [a4, a5, a6]
row3 = [a7, a8, a9]
A = array((row1, row2, row3), dtype=complex)

##set up solution array
v = array([x/R1,x/R2,x/R3],float)

v = solve(A,v)
